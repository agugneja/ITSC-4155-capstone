from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup
import requests
import json
from Model.model import faculty_members
import logging
from .liststream import liststream_handler
from typing import Optional





logger = logging.getLogger(__name__)
logger.addHandler(liststream_handler)
logger.setLevel(logging.INFO)

def scrape_all_faculty() -> None:
    """Scrapes contact info for all faculty and then updates the database"""
    emails = [faculty['email'] for faculty in faculty_members.find({"email":{"$exists":"true"}})]
    faculty = []

    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    with ThreadPoolExecutor(max_workers=15) as p:
        faculty = p.map(lambda letter: scrape_facstaff_by_name(letter, emails), alphabet)
    
    for lst in faculty:
        for info in lst:
            faculty_members.find_one_and_update({'email':info['email']}, {'$set':{'tel':info['tel'], 'address':info['address']}})

def scrape_facstaff_by_name(fname: str, emails: list[str]) -> list[dict[str, str]]:
    """Returns all contact info for names starting with fname"""
    page_num = 1
    logger.info(f'On page {page_num} of names starting with {fname.upper()}')
    url = 'https://directory.charlotte.edu/facstaff'

    results = []
    # make search
    form_data = {'fname': fname,
                 'op': 'Search',
                 'form_id': 'unc_charlotte_directory_facstaff_search_form'
                 }
    # scrape first page
    response = requests.post(url=url, data=form_data).text
    soup = BeautifulSoup(response, 'lxml')
    
    results += scrape_contact_info(soup, emails)
    
    # scrape additional pages
    while soup.find('button', value='Next Page'):
        
        page_num += 1
        logger.info(f'On page {page_num} of names starting with {fname.upper()}')
        # necessary to visit next page
        form_build_id = soup.find('input', attrs={'name':'form_build_id'})['value']
        form_data['form_build_id'] = form_build_id
        form_data['op'] = 'Next Page'

        response = requests.post(url=url, data=form_data).text
        soup = BeautifulSoup(response, 'lxml')
        results += scrape_contact_info(soup, emails)
    
    return results

def scrape_contact_info(soup: BeautifulSoup, emails: list[str]) -> list[dict[str,str]]:
    """Scrapes the contact info from a given facstaff page """
    contact_info = []
    for result in soup.find_all('div', class_='unc-charlotte-faculty-staff-search-form-result'):
        email_div = result.find('div', class_='unc-charlotte-faculty-staff-search-form-result-email')
        # if entry has an email and it's an email of a faculty member in our database
        if email_div is not None and email_div.text in emails:
            email = email_div.text
            # get phone number
            if phone_div := result.find('div', class_='unc-charlotte-faculty-staff-search-form-result-phone'):
                phone = phone_div.text
            else:
                phone = None
            # get address
            if address_div := result.find('div', class_='unc-charlotte-faculty-staff-search-form-result-address'):
                address = address_div.get_text(separator='\n')
            else:
                address = None

            contact_info.append({'email': email, 'tel': phone, 'address': address})

    return contact_info


def scrape_contact_info_by_email(fname, email) -> Optional[dict[str,str]]:
    """Scrapes all the possible pages of facstaff for the faculty member 
    specified by the email and first initial given"""
    page_num = 1
    logger.info(f'On page {page_num} of names starting with {fname.upper()}')
    url = 'https://directory.charlotte.edu/facstaff'

    # make search
    form_data = {'fname': fname,
                 'op': 'Search',
                 'form_id': 'unc_charlotte_directory_facstaff_search_form'
                 }
    # scrape first page
    response = requests.post(url=url, data=form_data).text
    soup = BeautifulSoup(response, 'lxml')
    if profile := find_profile_by_email(soup, email):
        return profile
     # scrape additional pages
    while soup.find('button', value='Next Page'):
        
        page_num += 1
        logger.info(f'On page {page_num} of names starting with {fname.upper()}')
        # necessary to visit next page
        form_build_id = soup.find('input', attrs={'name':'form_build_id'})['value']
        form_data['form_build_id'] = form_build_id
        form_data['op'] = 'Next Page'

        response = requests.post(url=url, data=form_data).text
        soup = BeautifulSoup(response, 'lxml')
        if profile := find_profile_by_email(soup, email):
            return profile
    logger.info(f'Finished with {fname.upper()}!')
    return None

def find_profile_by_email(soup, email) -> Optional[dict[str,str]]:
    """Scrapes an individual page to find the faculty member specified by the email"""
    for result in soup.find_all('div', class_='unc-charlotte-faculty-staff-search-form-result'):
        email_div = result.find('div', class_='unc-charlotte-faculty-staff-search-form-result-email')
        # if entry has an email and it's an email of a faculty member in our database
        if email_div is not None and email_div.text == email:
            # get phone number
            if phone_div := result.find('div', class_='unc-charlotte-faculty-staff-search-form-result-phone'):
                phone = phone_div.text
            else:
                phone = None
            # get address
            if address_div := result.find('div', class_='unc-charlotte-faculty-staff-search-form-result-address'):
                address = address_div.get_text(separator='\n')
            else:
                address = None

            return {'email': email, 'tel': phone, 'address': address}

    return None
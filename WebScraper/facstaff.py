from bs4 import BeautifulSoup
import requests
import json
from Model.model import faculty_members

emails = [faculty['email'] for faculty in faculty_members.find({"email":{"$exists":"true"}})]

def scrape_faculty_directory(fname: str) -> list[dict[str, str]]:
    page_num = 1
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
    
    results += scrape_contact_info(soup)
    
    # scrape additional pages
    while soup.find('button', value='Next Page'):
        
        page_num += 1
        print(f'on page {page_num} of {fname}')
        # necessary to visit next page
        form_build_id = soup.find('input', attrs={'name':'form_build_id'})['value']
        form_data['form_build_id'] = form_build_id
        form_data['op'] = 'Next Page'

        response = requests.post(url=url, data=form_data).text
        soup = BeautifulSoup(response, 'lxml')

        results += scrape_contact_info(soup)
    
    return results

def scrape_contact_info(soup: BeautifulSoup):

    contact_info = []
    for result in soup.find_all('div', class_='unc-charlotte-faculty-staff-search-form-result'):
        email_div = result.find('div', class_='unc-charlotte-faculty-staff-search-form-result-email')
        if email_div is not None and email_div.text in emails:
            email = email_div.text
            if phone_div := result.find('div', class_='unc-charlotte-faculty-staff-search-form-result-phone'):
                phone = phone_div.text
            else:
                phone = None
            if address_div := result.find('div', class_='unc-charlotte-faculty-staff-search-form-result-address'):
                address = address_div.get_text(separator='\n')
            else:
                address = None
            contact_info.append({'email': email, 'tel': phone, 'address': address})
    return contact_info

def scrape_all_faculty():
    faculty = []
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for letter in alphabet:
        faculty += scrape_faculty_directory(letter)

def parse_name(name: str) -> str:
    return ' '.join(' '.join(reversed(name.split(','))).split())

def main():
    for info in scrape_faculty_directory('f'):
        print(info)
        if faculty_members.find_one_and_update({'email':info['email']}, {'$set':{'tel':info['tel'], 'address':info['address']}}) is None:
            print("ASDADFSSDFS")
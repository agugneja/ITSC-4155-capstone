from scholarly import scholarly
from Model.model import faculty_members, update_by_name, FacultyProfile
from .liststream import liststream_handler
import logging 
from time import sleep
from random import randint, random
from bs4 import BeautifulSoup, Tag

logger = logging.getLogger(__name__)
logger.addHandler(liststream_handler)
logger.setLevel(logging.INFO)

def grab_profile_by_publisher_name(publisher_name):
    search_results = scholarly.search_author(publisher_name)
    for author in search_results:
        if 'UNC Charlotte' in author['affiliation'] or author['email_domain'] == '@uncc.edu':
            logger.info(f'Google Scholar profile for {publisher_name} found!')
            return f'https://scholar.google.com/citations?hl=en&user={author["scholar_id"]}'
        
    logger.info(f'No Google Scholar profile found for {publisher_name}')
    return None


def scrape_all_scholar_profiles():
    members = [FacultyProfile(**member) for member in faculty_members.find({'department': {'$exists':True}}, {'_id':False})]
    
    for member in members:
        if scholar_url := grab_profile_by_publisher_name(member.name):
            member.scholar_url = scholar_url
            member.rawHtml = insert_scholar_url_into_html(BeautifulSoup(member.rawHtml, 'lxml'), scholar_url)
        # random_sleep()
    
    update_by_name([members])
    
def insert_scholar_url_into_html(soup: BeautifulSoup, scholar_url):
    new_tag = BeautifulSoup(f'<div id="google_scholar_profile_link"><a href="{scholar_url}">Google Scholar Profile</a></div>','lxml').html.body.div
    if not (scholar_div := soup.find('div', {'id':'google_scholar_profile_link'})):
        print('made new')
        soup.append(new_tag)
    else:
        print('replaced')
        scholar_div.replaceWith(new_tag)
    return soup

def random_sleep():
    sleep(random())


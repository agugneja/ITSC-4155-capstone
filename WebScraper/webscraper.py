import requests
import inspect
from io import StringIO
from . import chhs, education, engineering, liberalscience, misc
from Model.model import FacultyProfile, update_by_name, update_last_update_time
from .FacultyWebScraper import FacultyWebScraper
from concurrent.futures import ThreadPoolExecutor
import csv
import sys
from contextlib import redirect_stdout
from .liststream import liststream_handler
import logging
from datetime import datetime, timezone
from time import sleep
from .facstaff import scrape_all_faculty, scrape_facstaff_by_name, scrape_contact_info_by_email

is_running = False
logger = logging.getLogger(__name__)
logger.addHandler(liststream_handler)
logger.setLevel(logging.INFO)

def scrape_department_profiles():
    # modules = [chhs, education, engineering, liberalscience, misc]
    modules = [education]
    departments = []
    for module in modules:
        for name, obj in inspect.getmembers(module, predicate=inspect.isclass):
            if obj is not FacultyWebScraper and issubclass(obj, FacultyWebScraper):
                departments.append(obj)
    
    department_objects = [x() for x in departments]
    with ThreadPoolExecutor(max_workers=15) as p:
        p.map(lambda x: x.run(), department_objects)

    profiles = []
    for d in department_objects:
        profiles += d.profiles
                

    # # site, type, action, title, excerpt, content, date, author, slug, status, menu-order, password, categories, tags, taxonomy-{name}, meta-{name}
    # header = ["site", "type", "action", "title", "excerpt", "content", "date", "author", "slug", "status", "menu-order", "password",
    #           "categories", "tags", "taxonomy-{name}", "meta-{name}"]

    # with open("post.csv", "a", newline="", encoding='utf-8') as f:
    #     writer = csv.writer(f)
    #     writer.writerow(header)

    #     # Writes to CSV based on specfic formatting defined in header list
    #     for profile in profiles:
    #         row = [profile.url, "post", "update", profile.name, "", profile.rawHtml, "", "", "", "", ""]
    #         writer.writerow(row)

    update_by_name(profiles)

def update_single(url: str, department: str, scrape_contact_info: bool):
    global is_running
    is_running = True

    for college in [chhs, education, engineering, liberalscience, misc]:
        if _class := getattr(college, department, None):
            department_class = _class
    logger.info('Starting department profile scrape...')
    updated_profile = department_class().scrapeSingle(url)

    if scrape_contact_info and updated_profile.email is not None:
        logger.info('Starting contact info scrape...')
        contact_info = scrape_contact_info_by_email(updated_profile.name[0], updated_profile.email)
        print(contact_info)
        # don't overwrite with None by accident 
        if contact_info['tel']:
            logger.info('Phone number found!')
            updated_profile.tel = contact_info['tel']
        if contact_info['address']:
            logger.info('Address found!')
            updated_profile.address = contact_info['address']
    
    update_by_name([updated_profile]) 
    is_running = False

def main(department_profiles: bool, contact_info: bool):
    global is_running
    is_running = True

    if department_profiles:
        logger.info('Starting department profile scrape...')
        scrape_department_profiles()
    if contact_info:
        logger.info('Starting contact info scrape...')
        scrape_all_faculty()

    is_running = False
    update_last_update_time(datetime.utcnow())

if __name__ == '__main__':
    scrape_department_profiles()

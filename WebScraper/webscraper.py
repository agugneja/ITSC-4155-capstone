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
is_running = False

def main():
    global is_running
    is_running = True
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
    update_last_update_time(datetime.utcnow())
    is_running = False

def update_single(url, department):
    global is_running
    is_running = True

    for college in [chhs, education, engineering, liberalscience, misc]:
        if _class := getattr(college, department, None):
            department_class = _class

    updated_profile = department_class().scrapeSingle(url)
    update_by_name([updated_profile]) 
    is_running = False

if __name__ == '__main__':
    main()

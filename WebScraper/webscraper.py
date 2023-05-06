import requests
import inspect
from io import StringIO
from . import chhs, education, engineering, liberalscience, misc
from Model.model import FacultyProfile, update_by_name
from .FacultyWebScraper import FacultyWebScraper
from concurrent.futures import ThreadPoolExecutor
import csv
import sys
from contextlib import redirect_stdout
from .liststream import liststream_handler
import logging
from datetime import datetime, timezone

is_running = False
last_updated = datetime.now(timezone.utc)

def main():
    global is_running, last_updated
    is_running = True
    # modules = [chhs, education, engineering, liberalscience, misc]
    modules = [chhs]
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
        # print(d.bad_urls)
                

    # site, type, action, title, excerpt, content, date, author, slug, status, menu-order, password, categories, tags, taxonomy-{name}, meta-{name}
    header = ["site", "type", "action", "title", "excerpt", "content", "date", "author", "slug", "status", "menu-order", "password",
              "categories", "tags", "taxonomy-{name}", "meta-{name}"]

    with open("post.csv", "a", newline="", encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(header)

        # Writes to CSV based on specfic formatting defined in header list
        for profile in profiles:
            row = [profile.url, "post", "update", profile.name, "", profile.rawHtml, "", "", "", "", ""]
            writer.writerow(row)

    update_by_name(profiles)
    last_updated = datetime.utcnow()
    is_running = False

def _main():
    main()
if __name__ == '__main__':
    main()

import requests
import inspect
from . import chhs, education, engineering, liberalscience, misc
from Model.model import FacultyProfile, update_by_name
from .FacultyWebScraper import FacultyWebScraper
from concurrent.futures import ThreadPoolExecutor
import csv

def main():
    modules = [chhs, education, engineering, liberalscience, misc]
    # modules = [education]
    departments = []
    for module in modules:
        for name, obj in inspect.getmembers(module, predicate=inspect.isclass):
            if obj is not FacultyWebScraper and issubclass(obj, FacultyWebScraper):
                departments.append(obj)
    
    with ThreadPoolExecutor(max_workers=15) as p:
        department_objects = list(p.map(lambda x: x(), departments))

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

if __name__ == '__main__':
    main()

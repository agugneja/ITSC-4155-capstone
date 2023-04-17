# Jacob Nyborg
from pkgutil import iter_modules
import requests
from . import Education
from . import Engineering
from . import CHHS
from . import LiberalScience
from . import Misc
from .LiberalScience import English
from Model.model import FacultyProfile, update_by_name
import importlib
from concurrent.futures import ThreadPoolExecutor
import csv

def is_url_valid(url: str) -> bool:
    try:
        requests.get(url)
    except Exception:
        return False
    return True

def main():
    packages = [CHHS, Education, Engineering, LiberalScience, Misc]
    departments = []
    # For each folder containing modules
    for package in packages:
        # For each module inside the folder
        for _, module_name, _ in iter_modules(package.__path__):
            module = importlib.import_module(f'{package.__name__}.{module_name}')
            # Each module contains a class with the same name as the module
            # This gets that class from the module
            departments.append(getattr(module, module_name))

    with ThreadPoolExecutor(max_workers=15) as p:
        department_objects = list(p.map(lambda x: x(), departments))

    profiles = []
    for d in department_objects:
        profiles += d.profiles
                

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

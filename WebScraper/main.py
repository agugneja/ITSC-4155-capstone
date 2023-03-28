# Jacob Nyborg
from pkgutil import iter_modules
import requests
import Education
import Engineering
import CHHS
import LiberalScience
import Misc
import importlib
from concurrent.futures import ThreadPoolExecutor
import csv
import itertools



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

    with ThreadPoolExecutor(max_workers=50) as p:
        department_objects = list(p.map(lambda x: x(), departments))

    # profileList = [d.profilePages if 'profilePages' in d.__dict__ else d.profiles for d in department_objects]  # List for Profile Page Content
    # profileList = list(itertools.chain.from_iterable(profileList))
    # urlList = [d.facultyURLs for d in department_objects]  # List for URLs to the faculty profiles

    # urlList = list(itertools.chain.from_iterable(urlList))
    profile_list = []
    url_list = []
    for d in department_objects:
        url_list += d.facultyURLs
        profile_list += d.profiles
    
    for i in range(len(url_list)-1, -1, -1):
        try:
            requests.get(url_list[i])
        except Exception:
            print("Removed URL: ", url_list[i])
            del url_list[i]
    

    # site, type, action, title, excerpt, content, date, author, slug, status, menu-order, password, categories, tags, taxonomy-{name}, meta-{name}
    header = ["site", "type", "action", "title", "excerpt", "content", "date", "author", "slug", "status", "menu-order", "password",
              "categories", "tags", "taxonomy-{name}", "meta-{name}"]

    with open("post.csv", "a", newline="", encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(header)

        # Writes to CSV based on specfic formatting defined in header list
        for i in range(len(profile_list)):
            listy = [url_list[i], "post", "update", profile_list[i]
                    ["Title"], "", profile_list[i]["Content"], "", "", "", "", ""]
            writer.writerow(listy)


if __name__ == '__main__':
    main()

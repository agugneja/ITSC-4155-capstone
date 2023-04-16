# Jacob Nyborg
from pkgutil import iter_modules
import requests
from . import Education
from . import Engineering
from . import CHHS
from . import LiberalScience
from . import Misc
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
    # packages = [CHHS, Education, Engineering, LiberalScience, Misc]
    packages = [CHHS]
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

    # profileList = [d.profilePages if 'profilePages' in d.__dict__ else d.profiles for d in department_objects]  # List for Profile Page Content
    # profileList = list(itertools.chain.from_iterable(profileList))
    # urlList = [d.facultyURLs for d in department_objects]  # List for URLs to the faculty profiles

    # urlList = list(itertools.chain.from_iterable(urlList))
    profile_list = []
    url_list = []
    for d in department_objects:
        url_list += d.facultyURLs
        profile_list += d.profiles
    
    bad_urls = []
    # with ThreadPoolExecutor(max_workers=25) as p:
    #     bad_urls_iterator = p.map(lambda x: x if not is_url_valid(x) else '', url_list)
    #     bad_urls = [url for url in bad_urls_iterator if url != '']

    # url_list = [(url if url not in bad_urls else '') for url in url_list ]
            

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
    
    # I know this is bad practice.
    # I will change this when web scrapers just use FacultyProfile instead of to janky parallel arrays.
    # This is also untested because my internet is slow.
    faculty_profiles = []
    for i in range(len(profile_list)): # 💩
        faculty_profiles.append(FacultyProfile(name=profile_list[i]['Title'], rawHtml=str(profile_list[i]["Content"]), url=url_list[i]))
    update_by_name(faculty_profiles)

if __name__ == '__main__':
    main()

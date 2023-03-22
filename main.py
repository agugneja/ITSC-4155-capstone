# Jacob Nyborg
from fileinput import close
from pkgutil import iter_modules
import inspect
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
    profileList = []
    urlList = []
    for d in department_objects:
        urlList += d.facultyURLs
        profileList += d.profiles
    
    for i in range(len(urlList)-1, -1, -1):
        try:
            requests.get(urlList[i])
        except Exception:
            print("Removed URL: ", urlList[i])
            del urlList[i]

    # site, type, action, title, excerpt, content, date, author, slug, status, menu-order, password, categories, tags, taxonomy-{name}, meta-{name}
    header = ["site", "type", "action", "title", "excerpt", "content", "date", "author", "slug", "status", "menu-order", "password",
              "categories", "tags", "taxonomy-{name}", "meta-{name}"]

    f = open("post.csv", "a", newline="", encoding='utf-8')

    writer = csv.writer(f)
    writer.writerow(header)

    # Writes to CSV based on specfic formatting defined in header list
    for i in range(len(profileList)):
        listy = [urlList[i], "post", "update", profileList[i]
                 ["Title"], "", profileList[i]["Content"], "", "", "", "", ""]
        writer.writerow(listy)

    f.close()


if __name__ == '__main__':
    main()

from . import chhs, education, engineering, liberalscience, misc
from .FacultyWebScraper import FacultyWebScraper

def main():
    url = 'https://cee.charlotte.edu//directory/james-e-amburgey-phd-pe'
    department = 'Chemistry'
    department_class: FacultyWebScraper = None
    for college in [chhs, education, engineering, liberalscience, misc]:
        if _class := getattr(college, department, None):
            department_class = _class

    x = department_class().getProfilePage([url])
    print(x)


if __name__ == '__main__':
    main()

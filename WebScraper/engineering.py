from bs4 import BeautifulSoup, ResultSet, Tag
from typing import Optional
from .FacultyWebScraper import FacultyWebScraper

class Civil(FacultyWebScraper):
    
    def __init__(self):
        self.baseURL = "https://cee.charlotte.edu/"
        self.directoryURLs = ["https://cee.charlotte.edu/directory-box"]

    def getRawHtml(self, soup: BeautifulSoup, url: str) -> Optional[Tag]:
        return soup.find("article", {"class": "node node-directory node-promoted clearfix"})

    def getName(self, soup: BeautifulSoup, url: str) -> Optional[Tag]:
        return soup.find("h1",{'class':'page-header'}).getText()
    
    def scrapeURLs(self, soup: BeautifulSoup) -> ResultSet:
        return soup.find_all("a", {"class": "button button-green button-small"})

class Dean(FacultyWebScraper):

    def __init__(self):
        self.baseURL =  "https://engr.charlotte.edu"
        self.directoryURLs = ["https://engr.charlotte.edu/directory-box/dean%27s-office"]

    def getRawHtml(self, soup: BeautifulSoup, url: str) -> Optional[Tag]:
        return soup.find("article", {"class": "node node-directory clearfix"})

    def getName(self, soup: BeautifulSoup, url: str) -> Optional[Tag]:
        return soup.find("h1",{'class':'page-header'}).getText()
    
    def scrapeURLs(self, soup: BeautifulSoup) -> ResultSet:
        return soup.find_all("a", {"class": "button button-green button-small"})
    
class EPIC(FacultyWebScraper):

    def __init__(self):
        self.baseURL = "https://epic.charlotte.edu"
        self.directoryURLs = ["https://epic.charlotte.edu/epic-staff/9"]

    def getRawHtml(self, soup: BeautifulSoup, url: str) -> Optional[Tag]:
        return soup.find("article", {"class": "node node-directory node-promoted clearfix"})

    def getName(self, soup: BeautifulSoup, url: str) -> Optional[Tag]:
        return soup.find("h1", {'class': 'page-header'}).getText()
    
    def scrapeURLs(self, soup: BeautifulSoup) -> ResultSet:
        return soup.find_all("a", href=True, alt=True, title=True)

class Electrical(FacultyWebScraper):

    def __init__(self):
        self.baseURL = "https://ece.charlotte.edu"
        self.directoryURLs = ["https://ece.charlotte.edu/directory/faculty",
                    'https://ece.charlotte.edu/directory/professors-emeriti',
                    'https://ece.charlotte.edu/directory/staff']

    def getRawHtml(self, soup: BeautifulSoup, url: str) -> Optional[Tag]:
        return soup.find("article", {"class": "node node-directory node-promoted clearfix"})

    def getName(self, soup: BeautifulSoup, url: str) -> Optional[Tag]:
        return soup.find("h1",{'class':'page-header'}).getText()
    
    def scrapeURLs(self, soup: BeautifulSoup) -> ResultSet:
        return soup.find_all("a", {"class": "button button-green button-small"})

class EngineeringTech(FacultyWebScraper):

    def __init__(self):
        self.baseURL = "https://et.charlotte.edu/"
        self.directoryURLs = ["https://et.charlotte.edu/directory-box"]

    def getRawHtml(self, soup: BeautifulSoup, url: str) -> Optional[Tag]:
        return soup.find("article", {"class": "node node-directory node-promoted clearfix"})

    def getName(self, soup: BeautifulSoup, url: str) -> Optional[Tag]:
        return soup.find("h1",{'class':'page-header'}).getText()
    
    def scrapeURLs(self, soup: BeautifulSoup) -> ResultSet:
        return soup.find_all("a", {"class": "button button-green button-small"})
    
class MOSAIC(FacultyWebScraper):

    def __init__(self):
        self.baseURL = "https://engrmosaic.charlotte.edu"
        self.directoryURLs = ["https://engrmosaic.charlotte.edu/directory-box"]

    def getRawHtml(self, soup: BeautifulSoup, url: str) -> Optional[Tag]:
        return soup.find("article", {"class": "node node-directory node-promoted clearfix"})

    def getName(self, soup: BeautifulSoup, url: str) -> Optional[Tag]:
        return soup.find("h1", {'class': 'page-header'}).getText()
    
    def scrapeURLs(self, soup: BeautifulSoup) -> ResultSet:
        return soup.find_all("a", {"class": "button button-green button-small"})

class Mechanical(FacultyWebScraper):

    def __init__(self):
        self.baseURL = "https://mees.charlotte.edu/"
        self.directoryURLs = ["https://mees.charlotte.edu/directory/faculty",
            'https://mees.charlotte.edu/directory-box/professors-emeriti',
            'https://mees.charlotte.edu/directory/staff']

    def getRawHtml(self, soup: BeautifulSoup, url: str) -> Optional[Tag]:
        return soup.find("article", {"class": "node node-directory node-promoted clearfix"})

    def getName(self, soup: BeautifulSoup, url: str) -> Optional[Tag]:
        return soup.find("h1", {'class': 'page-header'}).getText()
    
    def scrapeURLs(self, soup: BeautifulSoup) -> ResultSet:
        return soup.find_all("a", {"class": "button button-green button-small"})

class Motorsports(FacultyWebScraper):

    def __init__(self):
        self.baseURL = "https://motorsports.charlotte.edu"
        self.directoryURLs = ["https://motorsports.charlotte.edu/directory-box"]

    def getRawHtml(self, soup: BeautifulSoup, url: str) -> Optional[Tag]:
        return soup.find("article", {"class": "node node-directory node-promoted clearfix"})

    def getName(self, soup: BeautifulSoup, url: str) -> Optional[Tag]:
        return soup.find("h1", {'class': 'page-header'}).getText()
    
    def scrapeURLs(self, soup: BeautifulSoup) -> ResultSet:
        return soup.find_all("a", {"class": "button button-green button-small"})

class StudentDevelopment(FacultyWebScraper):

    def __init__(self):
        self.baseURL = "https://osds.charlotte.edu"
        self.directoryURLs = ["https://osds.charlotte.edu/directory-list/faculty-and-staff"]

    def getRawHtml(self, soup: BeautifulSoup, url: str) -> Optional[Tag]:
        return soup.find("article", {"class": "node node-directory node-promoted clearfix"})

    def getName(self, soup: BeautifulSoup, url: str) -> Optional[Tag]:
        return soup.find("h1", {'class': 'page-header'}).getText()
    
    def scrapeURLs(self, soup: BeautifulSoup) -> ResultSet:
        return soup.find_all("a", {"class": "button button-gray"})

class Systems(FacultyWebScraper):

    def __init__(self):
        self.baseURL = "https://seem.charlotte.edu"
        self.directoryURLs = ["https://seem.charlotte.edu/directory-box"]

    def getRawHtml(self, soup: BeautifulSoup, url: str) -> Optional[Tag]:
        return soup.find("article", {"class": "node node-directory node-promoted clearfix"})

    def getName(self, soup: BeautifulSoup, url: str) -> Optional[Tag]:
        return soup.find("h1", {'class': 'page-header'}).getText()
    
    def scrapeURLs(self, soup: BeautifulSoup) -> ResultSet:
        return soup.find_all("a", {"class": "button button-green button-small"})
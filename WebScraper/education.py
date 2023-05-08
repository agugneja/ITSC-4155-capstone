
from bs4 import BeautifulSoup, ResultSet, Tag
from typing import Optional
from .FacultyWebScraper import FacultyWebScraper

class Counseling(FacultyWebScraper):

    def __init__(self):
        self.baseURL = "https://counseling.charlotte.edu"
        self.directoryURLs = ["https://counseling.charlotte.edu/directory-list"]

    def getRawHtml(self, soup: BeautifulSoup, url: str) -> Optional[Tag]:
        return soup.find("article")
    
    def getName(self, soup: BeautifulSoup, url: str) -> Optional[Tag]:
        return soup.find("h1",{'class':'page-header'}).getText().split(",")[0]

    def scrapeURLs(self, soup: BeautifulSoup) -> ResultSet:
        return soup.find_all("a",{"class":"button button-gray"})

class EducationLeadership(FacultyWebScraper):

    def __init__(self):
        self.baseURL = "https://edld.charlotte.edu"
        self.directoryURLs = ["https://edld.charlotte.edu/directory-list"]

    def getRawHtml(self, soup: BeautifulSoup, url: str) -> Optional[Tag]:
        return soup.find("article")
    
    def getName(self, soup: BeautifulSoup, url: str) -> Optional[Tag]:
        return soup.find("h1",{'class':'page-header'}).getText().split(",")[0]
    
    def scrapeURLs(self, soup: BeautifulSoup) -> ResultSet:
        return soup.find_all("a",{"class":"button button-gray"})

class K12(FacultyWebScraper):

    def __init__(self):
        self.baseURL = "https://mdsk.charlotte.edu"
        self.directoryURLs = ["https://mdsk.charlotte.edu/directory-list"]

    def getRawHtml(self, soup: BeautifulSoup, url: str) -> Optional[Tag]:
        return soup.find("article")

    def getName(self, soup: BeautifulSoup, url: str) -> Optional[Tag]:
        return soup.find("h1",{'class':'page-header'}).getText().split(",")[0]
    
    def scrapeURLs(self, soup: BeautifulSoup) -> ResultSet:
        return soup.find_all("a",{"class":"button button-gray"})

class ReadingAndElementaryEducation(FacultyWebScraper):

    def __init__(self):
        self.baseURL = "https://reel.charlotte.edu"
        self.directoryURLs = ["https://reel.charlotte.edu/directory-list/faculty"]

    def getRawHtml(self, soup: BeautifulSoup, url: str) -> Optional[Tag]:
        return soup.find("article")

    def getName(self, soup: BeautifulSoup, url: str) -> Optional[Tag]:
        return soup.find("h1",{'class':'page-header'}).getText().split(",")[0]
        
    def scrapeURLs(self, soup: BeautifulSoup) -> ResultSet:
        return soup.find_all("a",{"class":"button button-gray"})

class SchoolAndCommunityPartnerships(FacultyWebScraper):

    def __init__(self):
        self.baseURL = "https://osacp.charlotte.edu"
        self.directoryURLs = ["https://osacp.charlotte.edu/directory-flip"]

    def getRawHtml(self, soup: BeautifulSoup, url: str) -> Optional[Tag]:
        return soup.find("article")

    def getName(self, soup: BeautifulSoup, url: str) -> Optional[Tag]:
        return soup.find("h1",{'class':'page-header'}).getText().split(",")[0]
    
    def scrapeURLs(self, soup: BeautifulSoup) -> ResultSet:
        return soup.select(".directory-back > a:last-of-type")

class SpecialEdAndChildDev(FacultyWebScraper):

    def __init__(self):
        self.baseURL = "https://spcd.charlotte.edu"
        self.directoryURLs = ["https://spcd.charlotte.edu/directory-table"]
    
    def getRawHtml(self, soup: BeautifulSoup, url: str) -> Optional[Tag]:
        return soup.find("article")

    def getName(self, soup: BeautifulSoup, url: str) -> Optional[Tag]:
        return soup.find("h1",{'class':'page-header'}).getText().split(",")[0]

    def scrapeURLs(self, soup: BeautifulSoup) -> ResultSet:
        return soup.select(".views-field-field-directory-read-more-link > a")
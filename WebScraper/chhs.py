from bs4 import BeautifulSoup, ResultSet, Tag
from typing import Optional
from .FacultyWebScraper import FacultyWebScraper

class ApplPhysHlthClinSciAndKinesiology(FacultyWebScraper):

    def __init__(self):
        self.baseURL = "https://aphcs.charlotte.edu"
        self.directoryURLs = ["https://aphcs.charlotte.edu/directory"]

    def getRawHtml(self, soup: BeautifulSoup, url: str) -> Optional[Tag]:
        return soup.find("article", {"class":"node node-directory node-promoted clearfix"})
    
    def getName(self, soup: BeautifulSoup, url: str) -> Optional[Tag]:
        return soup.find("h1",{'class':'page-header'}).getText().split(",")[0]
    
    def scrapeURLs(self, soup: BeautifulSoup) -> ResultSet:
        return soup.find_all("a",{"class":"button button-green"})

class CHHS(FacultyWebScraper):

    def __init__(self):
        self.baseURL = "https://health.charlotte.edu"
        self.directoryURLs = ["https://health.charlotte.edu/about-college/faculty-and-staff?items_per_page=All"]

    def getRawHtml(self, soup: BeautifulSoup, url: str) -> Optional[Tag]:
        return soup.find("article", {"class":"node node-directory node-promoted clearfix"})
    
    def getName(self, soup: BeautifulSoup, url: str) -> Optional[Tag]:
        return soup.find("h1",{'class':'page-header'}).getText().split(",")[0]
    
    def scrapeURLs(self, soup: BeautifulSoup):
        return soup.find_all("a",{"class":"button button-gray"})

class PublicHealthSciences(FacultyWebScraper):

    def __init__(self):
        self.baseURL = "https://publichealth.charlotte.edu"
        self.directoryURLs = ["https://publichealth.charlotte.edu/directory/3"]

    def getRawHtml(self, soup: BeautifulSoup, url: str) -> Optional[Tag]:
        return soup.find("article", {"class":"node node-directory node-promoted clearfix"})
    
    def getName(self, soup: BeautifulSoup, url: str) -> Optional[Tag]:
        return soup.find("h1",{'class':'page-header'}).getText().split(",")[0]
    
    def scrapeURLs(self, soup: BeautifulSoup):
        return soup.find_all("a",{"class":"thumbnail-link"})
    
class SchoolOfNursing(FacultyWebScraper):

    def __init__(self):
        self.baseURL = "https://nursing.charlotte.edu"
        self.directoryURLs = ["https://nursing.charlotte.edu/about-us/faculty-and-staff"]

    def getRawHtml(self, soup: BeautifulSoup, url: str) -> Optional[Tag]:
        return soup.find("article", {"class":"node node-directory node-promoted clearfix"})
    
    def getName(self, soup: BeautifulSoup, url: str) -> Optional[Tag]:
        return soup.find("h1",{'class':'page-header'}).getText().split(",")[0]
    
    def scrapeURLs(self, soup: BeautifulSoup):
        return soup.find_all("a",{"class":"button button-gray"})

class SchoolOfSocialWork(FacultyWebScraper):
    
    def __init__(self):
        self.baseURL = "https://socialwork.charlotte.edu"
        self.directoryURLs = ["https://socialwork.charlotte.edu/about-us/faculty-and-staff-directory"]

    def getRawHtml(self, soup: BeautifulSoup, url: str) -> Optional[Tag]:
        return soup.find("article", {"class":"node node-directory node-promoted clearfix"})
    
    def getName(self, soup: BeautifulSoup, url: str) -> Optional[Tag]:
        return soup.find("h1",{'class':'page-header'}).getText().split(",")[0]
    
    def scrapeURLs(self, soup: BeautifulSoup):
        return soup.find_all("a",{"class":"button button-green"})
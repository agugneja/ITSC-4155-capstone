
from bs4 import BeautifulSoup, ResultSet, Tag
from typing import Optional
from .FacultyWebScraper import FacultyWebScraper

class ArtsAndArch(FacultyWebScraper):
    
    def __init__(self):
        self.baseURL = "https://coaa.charlotte.edu/"
        self.directoryURLs = ["https://coaa.charlotte.edu/directory/faculty",
            "https://coaa.charlotte.edu/directory/part-time-faculty",
            "https://coaa.charlotte.edu/directory/adjunct-faculty",
            "https://coaa.charlotte.edu/directory/staff",
            "https://coaa.charlotte.edu/directory/emeritus"]

    def getRawHtml(self, soup: BeautifulSoup, url: str) -> Optional[Tag]:
        return soup.find("article", {"class": "node node-directory node-promoted clearfix"})

    def getName(self, soup: BeautifulSoup, url: str) -> Optional[Tag]:
        return soup.find("h1",{'class':'page-header'}).getText()
    
    def scrapeURLs(self, soup: BeautifulSoup) -> ResultSet:
        return soup.find_all("a",{"class":"thumbnail-link"})

class Belk(FacultyWebScraper):
    def __init__(self):
        self.baseURL = "https://belkcollege.charlotte.edu/"
        self.directoryURLs = ["https://belkcollege.charlotte.edu/directory"]
    
    def getRawHtml(self, soup: BeautifulSoup, url: str) -> Optional[Tag]:
        return soup.find("article", {"class":"node node-directory-custom node-promoted clearfix"})

    def getName(self, soup: BeautifulSoup, url: str) -> Optional[Tag]:
        return soup.find("h1",{'class':'page-header'}).getText()
    
    def scrapeURLs(self, soup: BeautifulSoup) -> ResultSet:
        return soup.find_all("a",{"class":"button-gray"})

class CCI(FacultyWebScraper):

    def __init__(self):
        self.baseURL = "https://cci.charlotte.edu"
        self.directoryURLs = ["https://cci.charlotte.edu/directory/faculty?items_per_page=All"]
    
    def getRawHtml(self, soup: BeautifulSoup, url: str) -> Optional[Tag]:
        return soup.find("article", {"class":"node node-directory clearfix"})

    def getName(self, soup: BeautifulSoup, url: str) -> Optional[Tag]:
        return soup.find("h1",{'class':'page-header'}).getText()
    
    def scrapeURLs(self, soup: BeautifulSoup) -> ResultSet:
        return soup.find_all("a",{"class":"button-gray"})

class DataScience(FacultyWebScraper):

    def __init__(self):
        self.baseURL = "https://datascience.charlotte.edu"
        self.directoryURLs = ["https://datascience.charlotte.edu/directory/faculty"]
    
    def getRawHtml(self, soup: BeautifulSoup, url: str) -> Optional[Tag]:
        return soup.find("article")

    def getName(self, soup: BeautifulSoup, url: str) -> Optional[Tag]:
        return soup.find("h1",{'class':'page-header'}).getText().split(',')[0]
    
    def scrapeURLs(self, soup: BeautifulSoup) -> ResultSet:
        return soup.find_all("a",{"class":"thumbnail-link"})
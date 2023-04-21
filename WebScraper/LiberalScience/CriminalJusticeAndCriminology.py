#Steven wilson/ Jacob Nyborg
import requests
from bs4 import BeautifulSoup
from Model.model import FacultyProfile
from ..FacultyWebScraper import FacultyWebScraper
class CriminalJusticeAndCriminology(FacultyWebScraper):

    def __init__(self):
        print("Starting Criminal Justice Lib Science")
        directoryURL = "https://criminaljustice.charlotte.edu/people/faculty"
        baseURL = "https://criminaljustice.charlotte.edu"
        
        self.facultyURLs = self.getFacultyURLs(baseURL, directoryURL)
        self.profiles = self.getProfilePage(self.facultyURLs)

    def getRawHtml(self, soup: BeautifulSoup, url: str):
        if 'pages' in url:
            return soup.find("div", {"id":"content_pane"})
        else:
            return soup.find("section", {"class":"col-sm-9"})
    
    def getName(self, soup: BeautifulSoup, url: str) -> str:
        if 'pages' in url:
            return soup.find("div",{'class':'name'}).getText().split(",")[0]
        else:
            return soup.find("h1",{'class':'page-header'}).getText().split(",")[0]
        
    def scrapeURLs(self, soup: BeautifulSoup) -> list[str]:
        return soup.find_all("a", {"class": "button button-gray"})
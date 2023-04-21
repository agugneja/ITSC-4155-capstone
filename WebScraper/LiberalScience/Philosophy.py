# Jacob Nyborg
import requests
from bs4 import BeautifulSoup
from Model.model import FacultyProfile
from ..FacultyWebScraper import FacultyWebScraper
class Philosophy(FacultyWebScraper):

    def __init__(self):
        print("Starting Philosophy Lib Science")
        directoryURL = "https://philosophy.charlotte.edu/directory-list/faculty"
        baseURL = "https://philosophy.charlotte.edu"
        
        self.facultyURLs = self.getFacultyURLs(baseURL, directoryURL)
        self.profiles = self.getProfilePage(self.facultyURLs)

    def getRawHtml(self, soup: BeautifulSoup, url: str):
        if 'pages' in url:
            return soup.find("div", {"class":"one-sidebar-width right-sidebar"})
        else:
            return soup.find("div", {"class":"col-sm-9"})
                    
    def getName(self, soup: BeautifulSoup, url: str):
         if 'pages' in url:
            return soup.find("div",{'class':'page-title'}).getText().split(",")[0]
         else:
            return soup.find("h1",{'class':'page-header'}).getText().split(",")[0]
                    
    def scrapeURLs(self, soup: BeautifulSoup) -> list[str]:
        return soup.find_all("a", {"class": "button button-gray"})
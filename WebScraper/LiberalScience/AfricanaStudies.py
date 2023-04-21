#Ozzy Toth
import requests
from bs4 import BeautifulSoup
from Model.model import FacultyProfile
from ..FacultyWebScraper import FacultyWebScraper

class AfricanaStudies(FacultyWebScraper):

    def __init__(self):
        print("Starting Africana Studies Lib Science")
        baseURL = "https://africana.charlotte.edu"
        directoryURL = "https://africana.charlotte.edu/people/full-time-faculty"

        self.facultyURLs = self.getFacultyURLs(baseURL, directoryURL)
        self.profiles = self.getProfilePage(self.facultyURLs)

    def getRawHtml(self, soup: BeautifulSoup, url: str):
        if 'clas' in url:
            return soup.find("div", {"class":"entry-content"})       
        elif items := soup.find("article", {"class":"node node-directory clearfix"}):
            return items
        else:
            return soup.find("section", {"class":"col-sm-9"})
                    
    def getName(self, soup: BeautifulSoup, url: str):
         if 'clas' in url:
            return soup.find("div",{'class':'name'}).getText().split(",")[0]
         else:
            return soup.find("h1",{'class':'page-header'}).getText().split(",")[0]
                    
    def scrapeURLs(self, soup: BeautifulSoup) -> list[str]:
        return soup.find_all("a", {"class": "button button-gray"})
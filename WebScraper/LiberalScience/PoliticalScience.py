# Dylan Toms
import requests
from bs4 import BeautifulSoup
from Model.model import FacultyProfile
from ..FacultyWebScraper import FacultyWebScraper
class PoliticalScience(FacultyWebScraper):

    def __init__(self):
        print("Starting Political Science")
        directoryURL = "https://politicalscience.charlotte.edu/directory-list/full-time-faculty"
        baseURL = "https://politicalscience.charlotte.edu/"
    
        self.facultyURLs = self.getFacultyURLs(baseURL, directoryURL)
        self.profiles = self.getProfilePage(self.facultyURLs)

    def getRawHtml(self, soup: BeautifulSoup, url: str):
        if 'clas' in url:
            return soup.find("div", {"class":"entry-content"})       
        else:
            return soup.find("article", {"class":"node node-directory node-promoted clearfix"})
                    
    def getName(self, soup: BeautifulSoup, url: str):
         if 'clas' in url:
            return soup.find("div",{'class':'name'}).getText().split(",")[0]
         else:
            return soup.find("h1",{'class':'page-header'}).getText().split(",")[0]
                    
    def scrapeURLs(self, soup: BeautifulSoup) -> list[str]:
        return soup.find_all("a", {"class": "button button-gray"})
#Steven wilson
import requests
from bs4 import BeautifulSoup
from Model.model import FacultyProfile
from ..FacultyWebScraper import FacultyWebScraper
class Anthropology(FacultyWebScraper):

    def __init__(self):
        print("Starting Antropology Lib Science")
        baseURL = "https://anthropology.charlotte.edu"
        directoryURL = "https://anthropology.charlotte.edu/people"
        
        self.facultyURLs = self.getFacultyURLs(baseURL, directoryURL)
        self.profiles = self.getProfilePage(self.facultyURLs)

    def getRawHtml(self, soup: BeautifulSoup, url: str):
        return soup.find("article", {"class": "node node-directory node-promoted clearfix"})

    def getName(self, soup: BeautifulSoup, url: str):
        return soup.find("h1",{'class':'page-header'}).getText().split(",")[0]
    
    def scrapeURLs(self, soup: BeautifulSoup) -> list[str]:
        return soup.select(".directory-back > a:last-of-type")
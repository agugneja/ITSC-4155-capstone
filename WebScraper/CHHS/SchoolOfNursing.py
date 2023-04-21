#Steven wilson
import requests
from bs4 import BeautifulSoup
from Model.model import FacultyProfile
from ..FacultyWebScraper import FacultyWebScraper

class SchoolOfNursing(FacultyWebScraper):

    def __init__(self):
        print("Starting Nursing CHHS")
        baseURL = "https://nursing.charlotte.edu"
        directoryURL = "https://nursing.charlotte.edu/about-us/faculty-and-staff"
        self.bad_urls = []

        self.facultyURLs = self.getFacultyURLs(baseURL, directoryURL)
        self.profiles = self.getProfilePage(self.facultyURLs)

    def getRawHtml(self, soup: BeautifulSoup, url: str = None):
        return soup.find("article", {"class":"node node-directory node-promoted clearfix"})
    
    def getName(self, soup: BeautifulSoup, url: str = None):
        return soup.find("h1",{'class':'page-header'}).getText().split(",")[0]
    
    def scrapeURLs(self, soup: BeautifulSoup):
        return soup.find_all("a",{"class":"button button-gray"})
    
import requests
from bs4 import BeautifulSoup
from Model.model import FacultyProfile
from ..FacultyWebScraper import FacultyWebScraper

class Systems(FacultyWebScraper):

    def __init__(self):
        print("Starting Systems Engineering")
        baseURL = "https://seem.charlotte.edu"
        directoryURL = "https://seem.charlotte.edu/directory-box"

        self.facultyURLs = self.getFacultyURLs(baseURL, directoryURL)
        self.profiles = self.getProfilePage(self.facultyURLs)

    def getRawHtml(self, soup: BeautifulSoup, url: str):
        return soup.find("article", {"class": "node node-directory node-promoted clearfix"})

    def getName(self, soup: BeautifulSoup, url: str):
        return soup.find("h1", {'class': 'page-header'}).getText()
    
    def scrapeURLs(self, soup: BeautifulSoup) -> list[str]:
        return soup.find_all("a", {"class": "button button-green button-small"})
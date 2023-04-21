#Steven wilson
import requests
from bs4 import BeautifulSoup
from Model.model import FacultyProfile
from ..FacultyWebScraper import FacultyWebScraper

class SchoolAndCommunityPartnerships(FacultyWebScraper):

    def __init__(self):
        print("Starting Community Education")
        baseURL = "https://osacp.charlotte.edu"
        directoryURL = "https://osacp.charlotte.edu/directory-flip"
     
        self.facultyURLs = self.getFacultyURLs(baseURL, directoryURL)
        self.profiles = self.getProfilePage(self.facultyURLs)

    def getRawHtml(self, soup: BeautifulSoup, url: str):
        return soup.find("article")

    def getName(self, soup: BeautifulSoup, url: str):
        return soup.find("h1",{'class':'page-header'}).getText().split(",")[0]
    
    def scrapeURLs(self, soup: BeautifulSoup) -> list[str]:
        return soup.select(".directory-back > a:last-of-type")
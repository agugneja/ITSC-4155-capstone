import requests
from bs4 import BeautifulSoup
from Model.model import FacultyProfile
from ..FacultyWebScraper import FacultyWebScraper

class Mechanical(FacultyWebScraper):

    def __init__(self):
        print("Starting Mechanical Engineering")
        baseURL = "https://mees.charlotte.edu/"
        #Main directory
        mainURL = "https://mees.charlotte.edu/directory/faculty"
        #Emeritus
        URLemeritus = 'https://mees.charlotte.edu/directory-box/professors-emeriti'
        #Staff directory - don't know if this is needed
        URLstaff = 'https://mees.charlotte.edu/directory/staff'

        
        self.facultyURLs = self.getFacultyURLs(baseURL, mainURL)
        self.facultyURLs += self.getFacultyURLs(baseURL, URLemeritus)
        self.facultyURLs += self.getFacultyURLs(baseURL, URLstaff)

        self.profiles = self.getProfilePage(self.facultyURLs)

    def getRawHtml(self, soup: BeautifulSoup, url: str):
        return soup.find("article", {"class": "node node-directory node-promoted clearfix"})

    def getName(self, soup: BeautifulSoup, url: str):
        return soup.find("h1", {'class': 'page-header'}).getText()
    
    def scrapeURLs(self, soup: BeautifulSoup) -> list[str]:
        return soup.find_all("a", {"class": "button button-green button-small"})
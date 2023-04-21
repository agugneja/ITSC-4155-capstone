#Steven wilson
import requests
from bs4 import BeautifulSoup
from Model.model import FacultyProfile
from ..FacultyWebScraper import FacultyWebScraper


class Counseling(FacultyWebScraper):

    def __init__(self):
        print("Starting Counseling Education")
        baseURL = "https://counseling.charlotte.edu"
        directoryURL = "https://counseling.charlotte.edu/directory-list"

        self.facultyURLs = self.getFacultyURLs(baseURL, directoryURL)
        self.profiles = self.getProfilePage(self.facultyURLs)

    def getRawHtml(self, soup: BeautifulSoup, url: str):
        return soup.find("article")
    
    def getName(self, soup: BeautifulSoup, url: str):
        return soup.find("h1",{'class':'page-header'}).getText().split(",")[0]

    def scrapeURLs(self, soup: BeautifulSoup) -> list[str]:
        return soup.find_all("a",{"class":"button button-gray"})
    
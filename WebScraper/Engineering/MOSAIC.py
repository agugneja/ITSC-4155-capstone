import requests
from bs4 import BeautifulSoup
from Model.model import FacultyProfile
from ..FacultyWebScraper import FacultyWebScraper

class MOSAIC(FacultyWebScraper):
    
    def getProfilePage(self, facultyURLs: list[str]) -> list[FacultyProfile]:
        profiles = []
        for url in facultyURLs:
            try:
                page = requests.get(url)
                soup = BeautifulSoup(page.content, "lxml")

                rawHtml = soup.find("article", {"class": "node node-directory node-promoted clearfix"})
                name = soup.find("h1", {'class': 'page-header'}).getText()

                profiles.append(FacultyProfile(name=name, rawHtml=rawHtml, url=url))
            except Exception as e:
                print(f"Something went wrong when visiting {url}:")
                print(e)
        return profiles

    def __init__(self):
        print("Starting MOSAIC Engineering")
        baseURL = "https://engrmosaic.charlotte.edu"
        URL = "https://engrmosaic.charlotte.edu/directory-box"

        html_text = requests.get(URL)
        soup = BeautifulSoup(html_text.content, "lxml")

        self.facultyURLs = self.getFacultyURLs(baseURL, soup.find_all(
            "a", {"class": "button button-green button-small"}))
        self.profiles = self.getProfilePage(self.facultyURLs)
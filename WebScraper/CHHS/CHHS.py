#Steven wilson and Jacob Nyborg

import requests
from bs4 import BeautifulSoup
from Model.model import FacultyProfile
from ..FacultyWebScraper import FacultyWebScraper

class CHHS(FacultyWebScraper):

    def getProfilePage(self, facultyURLs: list[str]) -> list[FacultyProfile]:
        profiles = []
        for url in facultyURLs:
            try:
                page = requests.get(url)
                soup = BeautifulSoup(page.content, "lxml")

                rawHtml = soup.find("article", {"class":"node node-directory node-promoted clearfix"})
                name = soup.find("h1",{'class':'page-header'}).getText().split(",")[0]

                profiles.append(FacultyProfile(name=name, rawHtml=str(rawHtml), url=url))
            except Exception as e:
                print(f"Something went wrong when visiting {url}:")
                print(e)
        return profiles

    def __init__(self):
        print("Starting CHHS")
        baseURL = "https://health.charlotte.edu"
        directoryURL = "https://health.charlotte.edu/about-college/faculty-and-staff?items_per_page=All"

        html_text = requests.get(directoryURL)
        soup = BeautifulSoup(html_text.content, "lxml")

        self.facultyURLs = self.getFacultyURLs(baseURL, soup.find_all("a",{"class":"button button-gray"}))
        self.profiles = self.getProfilePage(self.facultyURLs)
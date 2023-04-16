#Steven wilson
import requests
from bs4 import BeautifulSoup
from Model.model import FacultyProfile
from .. import FacultyWebScraper

class SpecialEdAndChildDev(FacultyWebScraper.FacultyWebScraper):

    def getProfilePage(self) -> list[FacultyProfile]:
        profiles = []
        for url in self.facultyURLs:
            try:
                page = requests.get(url)
                soup = BeautifulSoup(page.content, "lxml")
                rawHtml = soup.find("article")
                name = soup.find("h1",{'class':'page-header'}).getText().split(",")[0]

                profiles.append(FacultyProfile(name=name, rawHtml=rawHtml, url=url))
            except Exception as e:
                print(f"Something went wrong when visiting {url}:")
                print(e)
        return profiles

    def __init__(self):
        print("Starting Special Education")
        baseURL = "https://spcd.charlotte.edu"
        directoryURL = "https://spcd.charlotte.edu/directory-table"
        
        html_text = requests.get(directoryURL)
        soup = BeautifulSoup(html_text.content, "lxml")

        self.facultyURLs = self.getFacultyURLs(baseURL, soup.select(".views-field-field-directory-read-more-link > a"))
        self.profiles = self.getProfilePage()
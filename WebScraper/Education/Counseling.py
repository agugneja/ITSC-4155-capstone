#Steven wilson
import requests
from bs4 import BeautifulSoup
from Model.model import FacultyProfile
from .. import FacultyWebScraper


class Counseling(FacultyWebScraper.FacultyWebScraper):

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
        print("Starting Counseling Education")
        baseURL = "https://counseling.charlotte.edu"
        directoryURL = "https://counseling.charlotte.edu/directory-list"
        
        html_text = requests.get(directoryURL)
        soup = BeautifulSoup(html_text.content, "lxml")

        self.facultyURLs = self.getFacultyURLs(baseURL, soup.find_all("a",{"class":"button button-gray"}))
        self.profiles = self.getProfilePage()
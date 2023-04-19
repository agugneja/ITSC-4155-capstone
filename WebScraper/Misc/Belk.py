import requests
from bs4 import BeautifulSoup
from Model.model import FacultyProfile
from ..FacultyWebScraper import FacultyWebScraper

class Belk(FacultyWebScraper):
    def __init__(self):
        print("Belk Started")
        baseURL = "https://belkcollege.charlotte.edu/"
        directoryURL = "https://belkcollege.charlotte.edu/directory"
        html_text = requests.get(directoryURL)
        soup = BeautifulSoup(html_text.content, "lxml")
        self.facultyURLs = self.getFacultyURLs(baseURL, soup.find_all("a",{"class":"button-gray"}))
        self.profiles = self.getProfilePage(self.facultyURLs)

    def getProfilePage(self, facultyURLs) -> list[FacultyProfile]:
        profiles = []
        for url in facultyURLs:
            try:
                page = requests.get(url)
                soup = BeautifulSoup(page.content, "lxml")

                rawHtml = soup.find("article", {"class":"node node-directory-custom node-promoted clearfix"})
                name = soup.find("h1",{'class':'page-header'}).getText()

                profiles.append(FacultyProfile(name=name, rawHtml=rawHtml, url=url))
            except Exception as e:
                print(f"Something went wrong when visiting {url}:")
                print(e)
        return profiles
import requests
from bs4 import BeautifulSoup
from Model.model import FacultyProfile
from ..FacultyWebScraper import FacultyWebScraper

class DataScience(FacultyWebScraper):
    def __init__(self):
        print("data science Started")
        baseURL = "https://datascience.charlotte.edu"
        directoryURL = "https://datascience.charlotte.edu/directory/faculty"
        html_text = requests.get(directoryURL)
        soup = BeautifulSoup(html_text.content, "lxml")
        self.facultyURLs = self.getFacultyURLs(baseURL, soup.find_all("a",{"class":"thumbnail-link"}))
        self.profiles = self.getProfilePage()

    def getProfilePage(self) -> list[FacultyProfile]:
        profiles = []
        for url in self.facultyURLs:
            try:
                page = requests.get(url)
                soup = BeautifulSoup(page.content, "lxml")

                rawHtml = soup.find("article", {"class":"node node-directory node-promoted clearfix"})
                name = soup.find("h1",{'class':'page-header'}).getText()

                profiles.append(FacultyProfile(name=name, rawHtml=rawHtml, url=url))
            except Exception as e:
                print(f"Something went wrong when visiting {url}:")
                print(e)
        return profiles
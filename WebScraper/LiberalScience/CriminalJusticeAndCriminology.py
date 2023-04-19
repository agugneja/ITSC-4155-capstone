#Steven wilson/ Jacob Nyborg
import requests
from bs4 import BeautifulSoup
from Model.model import FacultyProfile
from ..FacultyWebScraper import FacultyWebScraper
class CriminalJusticeAndCriminology(FacultyWebScraper):
    
    def getProfilePage(self, facultyURLs: list[str]) -> list[FacultyProfile]:
        profiles = []
        for url in facultyURLs:
            try:
                page = requests.get(url)
                soup = BeautifulSoup(page.content, "lxml")
                rawHtml = ''
                name = ''
                if 'pages' in url:
                    rawHtml = soup.find("div", {"id":"content_pane"})
                    name = soup.find("div",{'class':'name'}).getText().split(",")[0]
                else:
                    rawHtml = soup.find("section", {"class":"col-sm-9"})
                    name = soup.find("h1",{'class':'page-header'}).getText().split(",")[0]
                
                profiles.append(FacultyProfile(name=name, rawHtml=rawHtml, url=url))

            except Exception as e:
                print(f"Something went wrong when visiting {url}:")
                print(e)
        return profiles

    def __init__(self):
        print("Starting Criminal Justice Lib Science")
        directoryURL = "https://criminaljustice.charlotte.edu/people/faculty"
        baseURL = "https://criminaljustice.charlotte.edu"
        
        html_text = requests.get(directoryURL)
        soup = BeautifulSoup(html_text.content, "lxml")

        self.facultyURLs = self.getFacultyURLs(baseURL, soup.find_all(
            "a", {"class": "button button-gray"}))
        self.profiles = self.getProfilePage(self.facultyURLs)

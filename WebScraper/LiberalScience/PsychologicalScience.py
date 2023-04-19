#Jacob Nyborg
import requests
from bs4 import BeautifulSoup
from Model.model import FacultyProfile
from ..FacultyWebScraper import FacultyWebScraper
class PsychologicalScience(FacultyWebScraper):

    def getProfilePage(self, facultyURLs: list[str]) -> list[FacultyProfile]:
        profiles = []
        for url in facultyURLs:
            try:
                page = requests.get(url)
                soup = BeautifulSoup(page.content, "lxml")
                rawHtml = ''
                name = ''
                if 'clas' in url:
                    rawHtml = soup.find("div", {"class":"entry-content"})
                    name = soup.find("div",{'class':'name'}).getText().split(",")[0]
                elif items := soup.find("div", {"class":"region region-content"}):
                    rawHtml = items
                    name = soup.find("h1",{'class':'page-header'}).getText()
                else:
                    rawHtml = soup.find("section", {"class":"col-sm-9"})
                    name = soup.find("h1",{'class':'page-header'}).getText()
                
                # reverse comma seperated "last, first" name
                if ',' in name:
                    name = name.split(",")
                    name.reverse()
                    name = ' '.join([string.strip() for string in name])

                profiles.append(FacultyProfile(name=name, rawHtml=rawHtml, url=url))

            except Exception as e:
                print(f"Something went wrong when visiting {url}:")
                print(e)
        return profiles

    def __init__(self):
        print("Starting Global Studies Lib Science")
        directoryURL = "https://psych.charlotte.edu/people"
        baseURL = "https://psych.charlotte.edu"
    
        html_text = requests.get(directoryURL)
        soup = BeautifulSoup(html_text.content, "lxml")

        self.facultyURLs = self.getFacultyURLs(baseURL, soup.select(".directory-back > a:last-of-type"))
        self.profiles = self.getProfilePage(self.facultyURLs)
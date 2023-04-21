#Jacob Nyborg
import requests
from bs4 import BeautifulSoup
from Model.model import FacultyProfile
from ..FacultyWebScraper import FacultyWebScraper
class PsychologicalScience(FacultyWebScraper):

    def __init__(self):
        print("Starting Global Studies Lib Science")
        directoryURL = "https://psych.charlotte.edu/people"
        baseURL = "https://psych.charlotte.edu"
    
        self.facultyURLs = self.getFacultyURLs(baseURL, directoryURL)
        self.profiles = self.getProfilePage(self.facultyURLs)

    def getRawHtml(self, soup: BeautifulSoup, url: str):
        if 'clas' in url:
            return soup.find("div", {"class":"entry-content"})       
        elif items := soup.find("div", {"class":"region region-content"}):
            return items
        else:
            return soup.find("section", {"class":"col-sm-9"})
                    
    def getName(self, soup: BeautifulSoup, url: str):
        if 'clas' in url:
            name = soup.find("div",{'class':'name'}).getText().split(",")[0]
        else:
            name = soup.find("h1",{'class':'page-header'}).getText()
        
        # reverse comma seperated "last, first" formatted name
        if ',' in name:
            name = name.split(",")
            name.reverse()
            name = ' '.join([string.strip() for string in name])

        return name
         
    def scrapeURLs(self, soup: BeautifulSoup) -> list[str]:
        return soup.select(".directory-back > a:last-of-type")
#Jacob Nyborg
import requests
from bs4 import BeautifulSoup
from Model.model import FacultyProfile
from ..FacultyWebScraper import FacultyWebScraper
class ReligiousStudies(FacultyWebScraper):

    def __init__(self):
        print("Starting Religious Studies Lib Science")
        directoryURL = "https://religiousstudies.charlotte.edu/directory/faculty-and-staff"
        baseURL = "https://religiousstudies.charlotte.edu"
    
        self.facultyURLs = self.getFacultyURLs(baseURL, directoryURL)
        self.profiles = self.getProfilePage(self.facultyURLs)

    def getRawHtml(self, soup: BeautifulSoup, url: str):
        if 'clas' in url:
            return soup.find("div", {"class":"entry-content"})       
        elif items := soup.find("section", {"class":"col-sm-9"}):
            return items
        else:
            return soup.find("article", {"class":"node node-directory node-promoted clearfix"})
                    
    def getName(self, soup: BeautifulSoup, url: str):
         if 'clas' in url:
            return soup.find("div",{'class':'name'}).getText().split(",")[0]
         else:
            return soup.find("h1",{'class':'page-header'}).getText().split(",")[0]
                    
    def scrapeURLs(self, soup: BeautifulSoup) -> list[str]:
        return soup.select(".directory-back > a:last-of-type")
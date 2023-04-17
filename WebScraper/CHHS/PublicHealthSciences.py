#Steven wilson
import requests
from bs4 import BeautifulSoup
from Model.model import FacultyProfile
from ..FacultyWebScraper import FacultyWebScraper

class PublicHealthSciences(FacultyWebScraper):

    def getFacultyURLsEmeritus(self, baseURL, soup):
        URLs = []
        soupList = soup.find_all("a",{"class":"button button-green"})
        
        for i in soupList:
            href = i.get("href")
            profURL = baseURL + href if href.startswith('/') else href
            URLs.append(profURL)
        
        return URLs
    
    def getProfilePage(self) -> list[FacultyProfile]:
        profiles = []
        for url in self.facultyURLs:
            try:
                page = requests.get(url)
                soup = BeautifulSoup(page.content, "lxml")

                rawHtml = soup.find("article", {"class":"node node-directory node-promoted clearfix"})
                name = soup.find("h1",{'class':'page-header'}).getText().split(",")[0]

                profiles.append(FacultyProfile(name=name, rawHtml=rawHtml, url=url))
            except Exception as e:
                print(f"Something went wrong when visiting {url}:")
                print(e)
        return profiles

    def __init__(self):
        print("Starting Health Sciences CHSS")
        baseURL = "https://publichealth.charlotte.edu"
        directoryURL = "https://publichealth.charlotte.edu/directory/3"
        #Second directory is for Faculty Emeriti
        directoryURLEmeritus = "https://publichealth.charlotte.edu/about%20us/emeritus-faculty"    
        
        html_text = requests.get(directoryURL)
        soup = BeautifulSoup(html_text.content, "lxml")

        self.facultyURLs = self.getFacultyURLs(baseURL, soup.find_all("a",{"class":"thumbnail-link"}))
        self.profiles = self.getProfilePage()
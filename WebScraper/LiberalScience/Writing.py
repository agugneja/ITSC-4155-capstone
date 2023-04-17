#Jacob Nyborg
import requests
from bs4 import BeautifulSoup
from Model.model import FacultyProfile
from ..FacultyWebScraper import FacultyWebScraper
class Writing:

    #This page has the full url not extensions
    def getFacultyURLs(self, baseURL: str, soup: BeautifulSoup) -> list[str]:
        URLs = []
        soupList = soup.find_all("a",{"class":"thumbnail-link"})
        
        for a_tag in soupList:
            href = a_tag.get("href")
            profURL = baseURL + href if href.startswith('/') else href
            URLs.append(profURL)
        
        return URLs
    def getProfilePage(self) -> list[FacultyProfile]:
        profiles = []
        for url in self.facultyURLs:
            try:
                page = requests.get(url)
                soup = BeautifulSoup(page.content, "lxml")
                rawHtml = ''
                name = ''
                if 'clas' in url:
                    rawHtml = soup.find("div", {"class":"entry-content"})
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
        print("Starting Writing Lib Science")
        directoryURL = "https://writing.charlotte.edu/directory-grid/faculty"
        baseURL = "https://writing.charlotte.edu"
    
        html_text = requests.get(directoryURL)
        soup = BeautifulSoup(html_text.content, "lxml")

        self.facultyURLs = self.getFacultyURLs(baseURL, soup)
        self.profiles = self.getProfilePage()
#Steven wilson
import requests
from bs4 import BeautifulSoup
from Model.model import FacultyProfile

class SchoolOfNursing:

    def getFacultyURLs(self, baseURL: str, soup: BeautifulSoup) -> list[str]:
        URLs = []
        soupList = soup.find_all("a",{"class":"button button-gray"})
        
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

                rawHtml = soup.find("article", {"class":"node node-directory node-promoted clearfix"})
                name = soup.find("h1",{'class':'page-header'}).getText().split(",")[0]

                profiles.append(FacultyProfile(name=name, rawHtml=rawHtml, url=url))
            except Exception as e:
                print(f"Something went wrong when visiting {url}:")
                print(e)
        return profiles

    def __init__(self):
        print("Starting Nursing CHHS")
        baseURL = "https://nursing.charlotte.edu"
        directoryURL = "https://nursing.charlotte.edu/about-us/faculty-and-staff"
        #this school also has a directory for Faculty Emeriti but none have profiles

        html_text = requests.get(directoryURL)
        soup = BeautifulSoup(html_text.content, "lxml")

        self.facultyURLs = self.getFacultyURLs(baseURL, soup)
        self.profiles = self.getProfilePage()


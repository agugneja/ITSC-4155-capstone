#Steven wilson
import requests
from bs4 import BeautifulSoup
from Model.model import FacultyProfile

class ApplPhysHlthClinSciAndKinesiology:

    def getFacultyURLs(self, baseURL: str, soup: BeautifulSoup) -> list[str]:
        URLs = []
        soupList = soup.find_all("a",{"class":"button button-green"})
        
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
                soup = BeautifulSoup(page.content, "html.parser")

                rawHtml = soup.find("article", {"class":"node node-directory node-promoted clearfix"})
                name = soup.find("h1",{'class':'page-header'}).getText().split(",")[0]

                profiles.append(FacultyProfile(name=name, rawHtml=rawHtml, url=url))
            except Exception as e:
                print(f"Something went wrong when visiting {url}:")
                print(e)
        return profiles

    def __init__(self):
        print("ApplPhysHlthClinSciAndKinesiology CHHS")
        baseURL = "https://aphcs.charlotte.edu"
        directoryURL = "https://aphcs.charlotte.edu/directory"
        
        html_text = requests.get(directoryURL)
        soup = BeautifulSoup(html_text.content, "html.parser")

        self.facultyURLs = self.getFacultyURLs(baseURL, soup)
        self.profiles = self.getProfilePage()
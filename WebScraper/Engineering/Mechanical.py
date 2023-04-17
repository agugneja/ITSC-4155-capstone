import requests
from bs4 import BeautifulSoup
from Model.model import FacultyProfile
from ..FacultyWebScraper import FacultyWebScraper

class Mechanical:

    def getFacultyURLs(self, baseURL: str, soup: BeautifulSoup) -> list[str]:
        URLs = []
        soupList = soup.find_all(
            "a", {"class": "button button-green button-small"})
        
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

                rawHtml = soup.find("article", {"class": "node node-directory node-promoted clearfix"})
                name = soup.find("h1", {'class': 'page-header'}).getText()

                profiles.append(FacultyProfile(name=name, rawHtml=rawHtml, url=url))
            except Exception as e:
                print(f"Something went wrong when visiting {url}:")
                print(e)
        return profiles

    def __init__(self):
        print("Starting Mechanical Engineering")
        baseURL = "https://mees.charlotte.edu/"

        #Main directory
        URL = "https://mees.charlotte.edu/directory/faculty"
        #Emeritus
        URLemeritus = 'https://mees.charlotte.edu/directory-box/professors-emeriti'
        #Staff directory - don't know if this is needed
        URLstaff = 'https://mees.charlotte.edu/directory/staff'

        #Main directory
        html_text = requests.get(URL)
        soup = BeautifulSoup(html_text.content, "lxml")

        #Emeritus
        html_text = requests.get(URLemeritus)
        soup_Emeritus = BeautifulSoup(html_text.content, "lxml")

        #Staff directory 
        html_text = requests.get(URLstaff)
        soup_Staff = BeautifulSoup(html_text.content, "lxml")

        self.facultyURLs = self.getFacultyURLs(baseURL, soup)
        self.profiles = self.getProfilePage()

        self.emeritusURLs = self.getFacultyURLs(baseURL, soup_Emeritus)
        self.emeritusProfiles = self.getProfilePage(self.emeritusURLs)

        self.staffURLs = self.getFacultyURLs(baseURL, soup_Staff)
        self.staffProfiles = self.getProfilePage(self.staffURLs)

        self.facultyURLs += self.emeritusURLs
        self.facultyURLs += self.staffURLs

        self.profiles += self.emeritusProfiles
        self.profiles += self.staffProfiles

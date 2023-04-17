import requests
from bs4 import BeautifulSoup
from Model.model import FacultyProfile
from ..FacultyWebScraper import FacultyWebScraper

class Electrical(FacultyWebScraper):
    
    def getProfilePage(self, facultyURLs) -> list[FacultyProfile]:
        profiles = []
        for url in facultyURLs:
            try:
                page = requests.get(url)
                soup = BeautifulSoup(page.content, "lxml")

                rawHtml = soup.find("article", {"class": "node node-directory node-promoted clearfix"})
                name = soup.find("h1",{'class':'page-header'}).getText()

                profiles.append(FacultyProfile(name=name, rawHtml=rawHtml, url=url))
            except Exception as e:
                print(f"Something went wrong when visiting {url}:")
                print(e)
        return profiles


    def __init__(self):
        print("Starting Electrical Engineering")
        baseURL = "https://ece.charlotte.edu"

        #Main directory
        URL = "https://ece.charlotte.edu/directory/faculty"
        #Emeritus
        URLemeritus = 'https://ece.charlotte.edu/directory/professors-emeriti'
        #Staff directory - don't know if this is needed
        URLstaff = 'https://ece.charlotte.edu/directory/staff'

        #Main directory
        html_text = requests.get(URL)
        soup = BeautifulSoup(html_text.content, "lxml")

        #Emeritus
        html_text = requests.get(URLemeritus)
        soup_Emeritus = BeautifulSoup(html_text.content, "lxml")

        #Staff directory 
        html_text = requests.get(URLstaff)
        soup_Staff = BeautifulSoup(html_text.content, "lxml")

        self.facultyURLs = self.getFacultyURLs(baseURL, soup.find_all(
            "a", {"class": "button button-green button-small"}))
        self.profiles = self.getProfilePage(self.facultyURLs)

        self.emeritusURLs = self.getFacultyURLs(baseURL, soup_Emeritus.find_all(
            "a", {"class": "button button-green button-small"}))
        self.emeritusProfiles = self.getProfilePage(self.emeritusURLs)

        self.staffURLs = self.getFacultyURLs(baseURL, soup_Staff.find_all(
            "a", {"class": "button button-green button-small"}))
        self.staffProfiles = self.getProfilePage(self.staffURLs)

        self.facultyURLs += self.emeritusURLs
        self.facultyURLs += self.staffURLs

        self.profiles += self.emeritusProfiles
        self.profiles += self.staffProfiles
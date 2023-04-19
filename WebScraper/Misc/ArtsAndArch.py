import requests
from bs4 import BeautifulSoup
from Model.model import FacultyProfile
from ..FacultyWebScraper import FacultyWebScraper

class ArtsAndArch(FacultyWebScraper):
    def __init__(self):
        print("Starting Arts and Architecture")
        baseURL = "https://coaa.charlotte.edu/"
        
        self.facultyURLs = []
        URL = "https://coaa.charlotte.edu/directory/faculty"
        html_text = requests.get(URL)
        soup1 = BeautifulSoup(html_text.content, "lxml")
        self.facultyURLs += self.getFacultyURLs(baseURL, soup1.find_all("a",{"class":"thumbnail-link"}))

        partURL = "https://coaa.charlotte.edu/directory/part-time-faculty"
        html_text = requests.get(partURL)
        soup2 = BeautifulSoup(html_text.content, "lxml")
        self.facultyURLs += self.getFacultyURLs(baseURL, soup2.find_all("a",{"class":"thumbnail-link"}))
        
        adjuntURL = "https://coaa.charlotte.edu/directory/adjunct-faculty"
        html_text = requests.get(adjuntURL)
        soup3 = BeautifulSoup(html_text.content, "lxml")
        self.facultyURLs += self.getFacultyURLs(baseURL, soup3.find_all("a",{"class":"thumbnail-link"}))
        
        staffURL = "https://coaa.charlotte.edu/directory/staff"
        html_text = requests.get(staffURL)
        soup4 = BeautifulSoup(html_text.content, "lxml")
        self.facultyURLs += self.getFacultyURLs(baseURL, soup4.find_all("a",{"class":"thumbnail-link"}))
        
        emeritusURL = "https://coaa.charlotte.edu/directory/emeritus"
        html_text = requests.get(emeritusURL)
        soup5 = BeautifulSoup(html_text.content, "lxml")
        self.facultyURLs += self.getFacultyURLs(baseURL, soup5.find_all("a",{"class":"thumbnail-link"}))
        self.profiles = self.getProfilePage(self.facultyURLs)

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
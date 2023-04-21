
from bs4 import BeautifulSoup
from .FacultyWebScraper import FacultyWebScraper

class ArtsAndArch(FacultyWebScraper):
    def __init__(self):
        print("Starting Arts and Architecture")
        baseURL = "https://coaa.charlotte.edu/"
        mainURL = "https://coaa.charlotte.edu/directory/faculty"
        partURL = "https://coaa.charlotte.edu/directory/part-time-faculty"
        adjuntURL = "https://coaa.charlotte.edu/directory/adjunct-faculty"
        staffURL = "https://coaa.charlotte.edu/directory/staff"
        emeritusURL = "https://coaa.charlotte.edu/directory/emeritus"
        
        
        self.facultyURLs = self.getFacultyURLs(baseURL, mainURL)
        self.facultyURLs += self.getFacultyURLs(baseURL, partURL)
        self.facultyURLs += self.getFacultyURLs(baseURL, adjuntURL)
        self.facultyURLs += self.getFacultyURLs(baseURL, staffURL)
        self.facultyURLs += self.getFacultyURLs(baseURL, emeritusURL)

        self.profiles = self.getProfilePage(self.facultyURLs)
    
    def getRawHtml(self, soup: BeautifulSoup, url: str):
        return soup.find("article", {"class": "node node-directory node-promoted clearfix"})

    def getName(self, soup: BeautifulSoup, url: str):
        return soup.find("h1",{'class':'page-header'}).getText()
    
    def scrapeURLs(self, soup: BeautifulSoup) -> list[str]:
        return soup.find_all("a",{"class":"thumbnail-link"})

class Belk(FacultyWebScraper):
    def __init__(self):
        print("Belk Started")
        baseURL = "https://belkcollege.charlotte.edu/"
        directoryURL = "https://belkcollege.charlotte.edu/directory"

        self.facultyURLs = self.getFacultyURLs(baseURL, directoryURL)
        self.profiles = self.getProfilePage(self.facultyURLs)
    
    def getRawHtml(self, soup: BeautifulSoup, url: str):
        return soup.find("article", {"class":"node node-directory-custom node-promoted clearfix"})

    def getName(self, soup: BeautifulSoup, url: str):
        return soup.find("h1",{'class':'page-header'}).getText()
    
    def scrapeURLs(self, soup: BeautifulSoup) -> list[str]:
        return soup.find_all("a",{"class":"button-gray"})

class CCI(FacultyWebScraper):
    def __init__(self):
        print("CCI Started")
        baseURL = "https://cci.charlotte.edu"
        directoryURL = "https://cci.charlotte.edu/directory/faculty?items_per_page=All"
   
        self.facultyURLs = self.getFacultyURLs(baseURL, directoryURL)
        self.profiles = self.getProfilePage(self.facultyURLs)
    
    def getRawHtml(self, soup: BeautifulSoup, url: str):
        return soup.find("article", {"class":"node node-directory clearfix"})

    def getName(self, soup: BeautifulSoup, url: str):
        return soup.find("h1",{'class':'page-header'}).getText()
    
    def scrapeURLs(self, soup: BeautifulSoup) -> list[str]:
        return soup.find_all("a",{"class":"button-gray"})

class DataScience(FacultyWebScraper):
    def __init__(self):
        print("data science Started")
        baseURL = "https://datascience.charlotte.edu"
        directoryURL = "https://datascience.charlotte.edu/directory/faculty"
   
        self.facultyURLs = self.getFacultyURLs(baseURL, directoryURL)
        self.profiles = self.getProfilePage(self.facultyURLs)
    
    def getRawHtml(self, soup: BeautifulSoup, url: str):
        return soup.find("article", {"class":"node node-directory node-promoted clearfix"})

    def getName(self, soup: BeautifulSoup, url: str):
        return soup.find("h1",{'class':'page-header'}).getText()
    
    def scrapeURLs(self, soup: BeautifulSoup) -> list[str]:
        return soup.find_all("a",{"class":"thumbnail-link"})
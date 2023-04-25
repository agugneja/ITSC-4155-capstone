from bs4 import BeautifulSoup, ResultSet, Tag
from typing import Optional
from .FacultyWebScraper import FacultyWebScraper

class ApplPhysHlthClinSciAndKinesiology(FacultyWebScraper):
        
    def run(self):
        print("ApplPhysHlthClinSciAndKinesiology CHHS")
        baseURL = "https://aphcs.charlotte.edu"
        directoryURL = "https://aphcs.charlotte.edu/directory"
        self.bad_urls = []
   
        self.facultyURLs = self.getFacultyURLs(baseURL, directoryURL)
        self.profiles = self.getProfilePage(self.facultyURLs)

    def getRawHtml(self, soup: BeautifulSoup, url: str) -> Optional[Tag]:
        return soup.find("article", {"class":"node node-directory node-promoted clearfix"})
    
    def getName(self, soup: BeautifulSoup, url: str) -> Optional[Tag]:
        return soup.find("h1",{'class':'page-header'}).getText().split(",")[0]
    
    def scrapeURLs(self, soup: BeautifulSoup) -> ResultSet:
        return soup.find_all("a",{"class":"button button-green"})

class CHHS(FacultyWebScraper):

    def run(self):
        print("Starting CHHS")
        baseURL = "https://health.charlotte.edu"
        directoryURL = "https://health.charlotte.edu/about-college/faculty-and-staff?items_per_page=All"
        self.bad_urls = []

        self.facultyURLs = self.getFacultyURLs(baseURL, directoryURL)
        self.profiles = self.getProfilePage(self.facultyURLs)

    def getRawHtml(self, soup: BeautifulSoup, url: str) -> Optional[Tag]:
        return soup.find("article", {"class":"node node-directory node-promoted clearfix"})
    
    def getName(self, soup: BeautifulSoup, url: str) -> Optional[Tag]:
        return soup.find("h1",{'class':'page-header'}).getText().split(",")[0]
    
    def scrapeURLs(self, soup: BeautifulSoup):
        return soup.find_all("a",{"class":"button button-gray"})

class PublicHealthSciences(FacultyWebScraper):

    def run(self):
        print("Starting Health Sciences CHSS")
        baseURL = "https://publichealth.charlotte.edu"
        directoryURL = "https://publichealth.charlotte.edu/directory/3"
        self.bad_urls = []

        self.facultyURLs = self.getFacultyURLs(baseURL, directoryURL)
        self.profiles = self.getProfilePage(self.facultyURLs)

    def getRawHtml(self, soup: BeautifulSoup, url: str) -> Optional[Tag]:
        return soup.find("article", {"class":"node node-directory node-promoted clearfix"})
    
    def getName(self, soup: BeautifulSoup, url: str) -> Optional[Tag]:
        return soup.find("h1",{'class':'page-header'}).getText().split(",")[0]
    
    def scrapeURLs(self, soup: BeautifulSoup):
        return soup.find_all("a",{"class":"thumbnail-link"})
    
class SchoolOfNursing(FacultyWebScraper):

    def run(self):
        print("Starting Nursing CHHS")
        baseURL = "https://nursing.charlotte.edu"
        directoryURL = "https://nursing.charlotte.edu/about-us/faculty-and-staff"
        self.bad_urls = []

        self.facultyURLs = self.getFacultyURLs(baseURL, directoryURL)
        self.profiles = self.getProfilePage(self.facultyURLs)

    def getRawHtml(self, soup: BeautifulSoup, url: str) -> Optional[Tag]:
        return soup.find("article", {"class":"node node-directory node-promoted clearfix"})
    
    def getName(self, soup: BeautifulSoup, url: str) -> Optional[Tag]:
        return soup.find("h1",{'class':'page-header'}).getText().split(",")[0]
    
    def scrapeURLs(self, soup: BeautifulSoup):
        return soup.find_all("a",{"class":"button button-gray"})

class SchoolOfSocialWork(FacultyWebScraper):

    def run(self):
        print("Starting Social Work CHHS")
        baseURL = "https://socialwork.charlotte.edu"
        directoryURL = "https://socialwork.charlotte.edu/about-us/faculty-and-staff-directory"
        self.bad_urls = []

        self.facultyURLs = self.getFacultyURLs(baseURL, directoryURL)
        self.profiles = self.getProfilePage(self.facultyURLs)

    def getRawHtml(self, soup: BeautifulSoup, url: str) -> Optional[Tag]:
        return soup.find("article", {"class":"node node-directory node-promoted clearfix"})
    
    def getName(self, soup: BeautifulSoup, url: str) -> Optional[Tag]:
        return soup.find("h1",{'class':'page-header'}).getText().split(",")[0]
    
    def scrapeURLs(self, soup: BeautifulSoup):
        return soup.find_all("a",{"class":"button button-green"})
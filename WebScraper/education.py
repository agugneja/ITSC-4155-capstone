
from bs4 import BeautifulSoup
from .FacultyWebScraper import FacultyWebScraper

class Counseling(FacultyWebScraper):

    def __init__(self):
        print("Starting Counseling Education")
        baseURL = "https://counseling.charlotte.edu"
        directoryURL = "https://counseling.charlotte.edu/directory-list"
    
        self.facultyURLs = self.getFacultyURLs(baseURL, directoryURL)
        self.profiles = self.getProfilePage(self.facultyURLs)

    def getRawHtml(self, soup: BeautifulSoup, url: str):
        return soup.find("article")
    
    def getName(self, soup: BeautifulSoup, url: str):
        return soup.find("h1",{'class':'page-header'}).getText().split(",")[0]

    def scrapeURLs(self, soup: BeautifulSoup) -> list[str]:
        return soup.find_all("a",{"class":"button button-gray"})

class EducationLeadership(FacultyWebScraper):

    def __init__(self):
        print("Starting Leadership Education")
        baseURL = "https://edld.charlotte.edu"
        directoryURL = "https://edld.charlotte.edu/directory-list"
        
        self.facultyURLs = self.getFacultyURLs(baseURL, directoryURL)
        self.profiles = self.getProfilePage(self.facultyURLs)

    def getRawHtml(self, soup: BeautifulSoup, url: str):
        return soup.find("article")
    
    def getName(self, soup: BeautifulSoup, url: str):
        return soup.find("h1",{'class':'page-header'}).getText().split(",")[0]
    
    def scrapeURLs(self, soup: BeautifulSoup) -> list[str]:
        return soup.find_all("a",{"class":"button button-gray"})

class K12(FacultyWebScraper):

    def __init__(self):
        print("Starting K12 Education")
        baseURL = "https://mdsk.charlotte.edu"
        directoryURL = "https://mdsk.charlotte.edu/directory-list"

        self.facultyURLs = self.getFacultyURLs(baseURL, directoryURL)
        self.profiles = self.getProfilePage(self.facultyURLs)

    def getRawHtml(self, soup: BeautifulSoup, url: str):
        return soup.find("article")

    def getName(self, soup: BeautifulSoup, url: str):
        return soup.find("h1",{'class':'page-header'}).getText().split(",")[0]
    
    def scrapeURLs(self, soup: BeautifulSoup) -> list[str]:
        return soup.find_all("a",{"class":"button button-gray"})

class ReadingAndElementaryEducation(FacultyWebScraper):

    def __init__(self):
        print("Starting Reading Education")
        baseURL = "https://reel.charlotte.edu"
        directoryURL = "https://reel.charlotte.edu/directory-list/faculty"
        
        self.facultyURLs = self.getFacultyURLs(baseURL, directoryURL)
        self.profiles = self.getProfilePage(self.facultyURLs)

    def getRawHtml(self, soup: BeautifulSoup, url: str):
        return soup.find("article")

    def getName(self, soup: BeautifulSoup, url: str):
        return soup.find("h1",{'class':'page-header'}).getText().split(",")[0]
        
    def scrapeURLs(self, soup: BeautifulSoup) -> list[str]:
        return soup.find_all("a",{"class":"button button-gray"})

class SchoolAndCommunityPartnerships(FacultyWebScraper):

    def __init__(self):
        print("Starting Community Education")
        baseURL = "https://osacp.charlotte.edu"
        directoryURL = "https://osacp.charlotte.edu/directory-flip"
     
        self.facultyURLs = self.getFacultyURLs(baseURL, directoryURL)
        self.profiles = self.getProfilePage(self.facultyURLs)

    def getRawHtml(self, soup: BeautifulSoup, url: str):
        return soup.find("article")

    def getName(self, soup: BeautifulSoup, url: str):
        return soup.find("h1",{'class':'page-header'}).getText().split(",")[0]
    
    def scrapeURLs(self, soup: BeautifulSoup) -> list[str]:
        return soup.select(".directory-back > a:last-of-type")

class SpecialEdAndChildDev(FacultyWebScraper):

    def __init__(self):
        print("Starting Special Education")
        baseURL = "https://spcd.charlotte.edu"
        directoryURL = "https://spcd.charlotte.edu/directory-table"
        
        self.facultyURLs = self.getFacultyURLs(baseURL, directoryURL)
        self.profiles = self.getProfilePage(self.facultyURLs)
    
    def getRawHtml(self, soup: BeautifulSoup, url: str):
        return soup.find("article")

    def getName(self, soup: BeautifulSoup, url: str):
        return soup.find("h1",{'class':'page-header'}).getText().split(",")[0]

    def scrapeURLs(self, soup: BeautifulSoup) -> list[str]:
        return soup.select(".views-field-field-directory-read-more-link > a")
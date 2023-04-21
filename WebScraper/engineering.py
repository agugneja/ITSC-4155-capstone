from bs4 import BeautifulSoup
from .FacultyWebScraper import FacultyWebScraper

class Civil(FacultyWebScraper):

    def __init__(self):
        print("Starting Civil Engineering")
        baseURL = "https://cee.charlotte.edu/"
        directoryURL = "https://cee.charlotte.edu/directory-box"

        self.facultyURLs = self.getFacultyURLs(baseURL, directoryURL)
        self.profiles = self.getProfilePage(self.facultyURLs)

    def getRawHtml(self, soup: BeautifulSoup, url: str):
        return soup.find("article", {"class": "node node-directory node-promoted clearfix"})

    def getName(self, soup: BeautifulSoup, url: str):
        return soup.find("h1",{'class':'page-header'}).getText()
    
    def scrapeURLs(self, soup: BeautifulSoup) -> list[str]:
        return soup.find_all("a", {"class": "button button-green button-small"})

class Dean(FacultyWebScraper):

    def __init__(self):
        print("Starting Dean Engineering")
        baseURL = "https://engr.charlotte.edu"
        directoryURL = "https://engr.charlotte.edu/directory-box/dean%27s-office"

        self.facultyURLs = self.getFacultyURLs(baseURL, directoryURL)
        self.profiles = self.getProfilePage(self.facultyURLs)

    def getRawHtml(self, soup: BeautifulSoup, url: str):
        return soup.find("article", {"class": "node node-directory clearfix"})

    def getName(self, soup: BeautifulSoup, url: str):
        return soup.find("h1",{'class':'page-header'}).getText()
    
    def scrapeURLs(self, soup: BeautifulSoup) -> list[str]:
        return soup.find_all("a", {"class": "button button-green button-small"})
    
class EPIC(FacultyWebScraper):

    def __init__(self):
        print("Starting Epic Engineering")
        baseURL = "https://epic.charlotte.edu"
        directoryURL = "https://epic.charlotte.edu/epic-staff/9"

        self.facultyURLs = self.getFacultyURLs(baseURL, directoryURL)
        self.profiles = self.getProfilePage(self.facultyURLs)

    def getRawHtml(self, soup: BeautifulSoup, url: str):
        return soup.find("article", {"class": "node node-directory node-promoted clearfix"})

    def getName(self, soup: BeautifulSoup, url: str):
        return soup.find("h1", {'class': 'page-header'}).getText()
    
    def scrapeURLs(self, soup: BeautifulSoup) -> list[str]:
        return soup.find_all("a", href=True, alt=True, title=True)

class Electrical(FacultyWebScraper):

    def __init__(self):
        print("Starting Electrical Engineering")
        baseURL = "https://ece.charlotte.edu"

        #Main directory
        mainURL = "https://ece.charlotte.edu/directory/faculty"
        #Emeritus
        URLemeritus = 'https://ece.charlotte.edu/directory/professors-emeriti'
        #Staff directory - don't know if this is needed
        URLstaff = 'https://ece.charlotte.edu/directory/staff'


        self.facultyURLs = self.getFacultyURLs(baseURL, mainURL)
        self.facultyURLs += self.getFacultyURLs(baseURL, URLemeritus)
        self.facultyURLs += self.getFacultyURLs(baseURL, URLstaff)

        self.profiles = self.getProfilePage(self.facultyURLs)

    def getRawHtml(self, soup: BeautifulSoup, url: str):
        return soup.find("article", {"class": "node node-directory node-promoted clearfix"})

    def getName(self, soup: BeautifulSoup, url: str):
        return soup.find("h1",{'class':'page-header'}).getText()
    
    def scrapeURLs(self, soup: BeautifulSoup) -> list[str]:
        return soup.find_all("a", {"class": "button button-green button-small"})

class EngineeringTech(FacultyWebScraper):

    def __init__(self):
        print("Starting Tech Engineering")
        baseURL = "https://et.charlotte.edu/"
        directoryURL = "https://et.charlotte.edu/directory-box"

        self.facultyURLs = self.getFacultyURLs(baseURL, directoryURL)
        self.profiles = self.getProfilePage(self.facultyURLs)

    def getRawHtml(self, soup: BeautifulSoup, url: str):
        return soup.find("article", {"class": "node node-directory node-promoted clearfix"})

    def getName(self, soup: BeautifulSoup, url: str):
        return soup.find("h1",{'class':'page-header'}).getText()
    
    def scrapeURLs(self, soup: BeautifulSoup) -> list[str]:
        return soup.find_all("a", {"class": "button button-green button-small"})
    
class MOSAIC(FacultyWebScraper):

    def __init__(self):
        print("Starting MOSAIC Engineering")
        baseURL = "https://engrmosaic.charlotte.edu"
        directoryURL = "https://engrmosaic.charlotte.edu/directory-box"

        self.facultyURLs = self.getFacultyURLs(baseURL, directoryURL)
        self.profiles = self.getProfilePage(self.facultyURLs)

    def getRawHtml(self, soup: BeautifulSoup, url: str):
        return soup.find("article", {"class": "node node-directory node-promoted clearfix"})

    def getName(self, soup: BeautifulSoup, url: str):
        return soup.find("h1", {'class': 'page-header'}).getText()
    
    def scrapeURLs(self, soup: BeautifulSoup) -> list[str]:
        return soup.find_all("a", {"class": "button button-green button-small"})

class Mechanical(FacultyWebScraper):

    def __init__(self):
        print("Starting Mechanical Engineering")
        baseURL = "https://mees.charlotte.edu/"
        #Main directory
        mainURL = "https://mees.charlotte.edu/directory/faculty"
        #Emeritus
        URLemeritus = 'https://mees.charlotte.edu/directory-box/professors-emeriti'
        #Staff directory - don't know if this is needed
        URLstaff = 'https://mees.charlotte.edu/directory/staff'

        
        self.facultyURLs = self.getFacultyURLs(baseURL, mainURL)
        self.facultyURLs += self.getFacultyURLs(baseURL, URLemeritus)
        self.facultyURLs += self.getFacultyURLs(baseURL, URLstaff)

        self.profiles = self.getProfilePage(self.facultyURLs)

    def getRawHtml(self, soup: BeautifulSoup, url: str):
        return soup.find("article", {"class": "node node-directory node-promoted clearfix"})

    def getName(self, soup: BeautifulSoup, url: str):
        return soup.find("h1", {'class': 'page-header'}).getText()
    
    def scrapeURLs(self, soup: BeautifulSoup) -> list[str]:
        return soup.find_all("a", {"class": "button button-green button-small"})

class Motorsports(FacultyWebScraper):

    def __init__(self):
        print("Starting Motorsports Engineering")
        baseURL = "https://motorsports.charlotte.edu"
        directoryURL = "https://motorsports.charlotte.edu/directory-box"

        self.facultyURLs = self.getFacultyURLs(baseURL, directoryURL)
        self.profiles = self.getProfilePage(self.facultyURLs)

    def getRawHtml(self, soup: BeautifulSoup, url: str):
        return soup.find("article", {"class": "node node-directory node-promoted clearfix"})

    def getName(self, soup: BeautifulSoup, url: str):
        return soup.find("h1", {'class': 'page-header'}).getText()
    
    def scrapeURLs(self, soup: BeautifulSoup) -> list[str]:
        return soup.find_all("a", {"class": "button button-green button-small"})

class StudentDevelopment(FacultyWebScraper):

    def __init__(self):
        print("Starting Student Development Engineering")
        baseURL = "https://osds.charlotte.edu"
        directoryURL = "https://osds.charlotte.edu/directory-list/faculty-and-staff"

        self.facultyURLs = self.getFacultyURLs(baseURL, directoryURL)
        self.profiles = self.getProfilePage(self.facultyURLs)

    def getRawHtml(self, soup: BeautifulSoup, url: str):
        return soup.find("article", {"class": "node node-directory node-promoted clearfix"})

    def getName(self, soup: BeautifulSoup, url: str):
        return soup.find("h1", {'class': 'page-header'}).getText()
    
    def scrapeURLs(self, soup: BeautifulSoup) -> list[str]:
        return soup.find_all("a", {"class": "button button-gray"})

class Systems(FacultyWebScraper):

    def __init__(self):
        print("Starting Systems Engineering")
        baseURL = "https://seem.charlotte.edu"
        directoryURL = "https://seem.charlotte.edu/directory-box"

        self.facultyURLs = self.getFacultyURLs(baseURL, directoryURL)
        self.profiles = self.getProfilePage(self.facultyURLs)

    def getRawHtml(self, soup: BeautifulSoup, url: str):
        return soup.find("article", {"class": "node node-directory node-promoted clearfix"})

    def getName(self, soup: BeautifulSoup, url: str):
        return soup.find("h1", {'class': 'page-header'}).getText()
    
    def scrapeURLs(self, soup: BeautifulSoup) -> list[str]:
        return soup.find_all("a", {"class": "button button-green button-small"})
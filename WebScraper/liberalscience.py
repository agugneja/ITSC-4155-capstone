
from bs4 import BeautifulSoup, ResultSet, Tag
from typing import Optional
from .FacultyWebScraper import FacultyWebScraper

class AfricanaStudies(FacultyWebScraper):

    def __init__(self):
        self.baseURL = "https://africana.charlotte.edu"
        self.directoryURLs = ["https://africana.charlotte.edu/people/full-time-faculty"]

    def getRawHtml(self, soup: BeautifulSoup, url: str) -> Optional[Tag]:
        if 'clas' in url:
            return soup.find("div", {"class":"entry-content"})       
        elif items := soup.find("article", {"class":"node node-directory clearfix"}):
            return items
        else:
            return soup.find("section", {"class":"col-sm-9"})
                    
    def getName(self, soup: BeautifulSoup, url: str) -> Optional[Tag]:
         if 'clas' in url:
            return soup.find("div",{'class':'name'}).getText().split(",")[0]
         else:
            return soup.find("h1",{'class':'page-header'}).getText().split(",")[0]
                    
    def scrapeURLs(self, soup: BeautifulSoup) -> ResultSet:
        return soup.find_all("a", {"class": "button button-gray"})
    
class Anthropology(FacultyWebScraper):

    def __init__(self):
        self.baseURL = "https://anthropology.charlotte.edu"
        self.directoryURLs = ["https://anthropology.charlotte.edu/people"]

    def getRawHtml(self, soup: BeautifulSoup, url: str) -> Optional[Tag]:
        return soup.find("article", {"class": "node node-directory node-promoted clearfix"})

    def getName(self, soup: BeautifulSoup, url: str) -> Optional[Tag]:
        return soup.find("h1",{'class':'page-header'}).getText().split(",")[0]
    
    def scrapeURLs(self, soup: BeautifulSoup) -> ResultSet:
        return soup.select(".directory-back > a:last-of-type")
    
class BiologicalSciences(FacultyWebScraper):

    def __init__(self):
        self.baseURL = "https://biology.charlotte.edu"
        self.directoryURLs = ["https://biology.charlotte.edu/directory/faculty"]

    def getRawHtml(self, soup: BeautifulSoup, url: str) -> Optional[Tag]:
        return soup.find("article", {"class": "node node-directory node-promoted clearfix"})

    def getName(self, soup: BeautifulSoup, url: str) -> Optional[Tag]:
        return soup.find("h1",{'class':'page-header'}).getText().split(",")[0]
    
    def scrapeURLs(self, soup: BeautifulSoup) -> ResultSet:
        return soup.select(".caption > a")

class Chemistry(FacultyWebScraper):

    def __init__(self):
        self.baseURL = "https://chemistry.charlotte.edu"
        self.directoryURLs = ["https://chemistry.charlotte.edu/directory-grid/faculty"]

    def getRawHtml(self, soup: BeautifulSoup, url: str) -> Optional[Tag]:
        return soup.find("article", {"class": "node node-directory node-promoted clearfix"})

    def getName(self, soup: BeautifulSoup, url: str) -> Optional[Tag]:
        return soup.find("h1",{'class':'page-header'}).getText().split(",")[0]
    
    def scrapeURLs(self, soup: BeautifulSoup) -> ResultSet:
        return soup.find_all("a",{"class":"thumbnail-link"})

class Communication(FacultyWebScraper):

    def __init__(self):
        self.baseURL = "https://communication.charlotte.edu"
        self.directoryURLs = ["https://communication.charlotte.edu/people/full-time-faculty"]

    def getRawHtml(self, soup: BeautifulSoup, url: str) -> Optional[Tag]:
        if 'clas' in url:
            return soup.find("div", {"class":"entry-content"})       
        elif items := soup.find("article", {"class":"node node-directory clearfix"}):
            return items
        else:
            return soup.find("section", {"class":"col-sm-9"})
                    
    def getName(self, soup: BeautifulSoup, url: str) -> Optional[Tag]:
         if 'clas' in url:
            return soup.find("div",{'class':'name'}).getText().split(",")[0]
         else:
            return soup.find("h1",{'class':'page-header'}).getText().split(",")[0]
                    
    def scrapeURLs(self, soup: BeautifulSoup) -> ResultSet:
        return soup.find_all("a", {"class": "button button-gray"})
    
class CriminalJusticeAndCriminology(FacultyWebScraper):

    def __init__(self):
        self.baseURL = baseURL = "https://criminaljustice.charlotte.edu"
        self.directoryURLs = ["https://criminaljustice.charlotte.edu/people/faculty"]

    def getRawHtml(self, soup: BeautifulSoup, url: str) -> Optional[Tag]:
        if 'pages' in url:
            return soup.find("div", {"id":"content_pane"})
        else:
            return soup.find("section", {"class":"col-sm-9"})
    
    def getName(self, soup: BeautifulSoup, url: str) -> str:
        if 'pages' in url:
            return soup.find("div",{'class':'name'}).getText().split(",")[0]
        else:
            return soup.find("h1",{'class':'page-header'}).getText().split(",")[0]
        
    def scrapeURLs(self, soup: BeautifulSoup) -> ResultSet:
        return soup.find_all("a", {"class": "button button-gray"})

class English(FacultyWebScraper):

    def __init__(self):
        self.baseURL = "https://english.charlotte.edu"
        self.directoryURLs = ["https://english.charlotte.edu/directory-list/professorial-faculty"]
    
    def getRawHtml(self, soup: BeautifulSoup, url: str) -> Optional[Tag]:
        if 'clas' in url:
            return soup.find("div", {"class":"entry-content"})
        else:
            return soup.find("article", {"class":"node node-directory node-promoted clearfix"}) 
    
    def getName(self, soup: BeautifulSoup, url: str) -> str:
        if 'clas' in url:
            return soup.find("div",{'class':'name'}).getText().split(",")[0]
        else:
            return soup.find("h1",{'class':'page-header'}).getText().split(",")[0]
        
    def scrapeURLs(self, soup: BeautifulSoup) -> ResultSet:
        return soup.find_all("a", {"class": "button button-gray"})

class Geography(FacultyWebScraper):

    def __init__(self):
        self.baseURL = "https://geoearth.charlotte.edu"
        self.directoryURLs = ["https://geoearth.charlotte.edu/directory-flip/full-time-faculty"]

    def getRawHtml(self, soup: BeautifulSoup, url: str) -> Optional[Tag]:
        if 'clas' in url:
            return soup.find("div", {"class":"entry-content"})       
        elif items := soup.find("article", {"class":"node node-directory clearfix"}):
            return items
        else:
            return soup.find("article", {"class":"node node-directory node-promoted clearfix"})
                    
    def getName(self, soup: BeautifulSoup, url: str) -> Optional[Tag]:
         if 'clas' in url:
            return soup.find("div",{'class':'name'}).getText().split(",")[0]
         else:
            return soup.find("h1",{'class':'page-header'}).getText().split(",")[0]
                    
    def scrapeURLs(self, soup: BeautifulSoup) -> ResultSet:
        return soup.select(".directory-back > a:last-of-type")
    
class GlobalStudies(FacultyWebScraper):

    def __init__(self):
        self.baseURL = "https://globalstudies.charlotte.edu"
        self.directoryURLs = ["https://globalstudies.charlotte.edu/people"]

    def getRawHtml(self, soup: BeautifulSoup, url: str) -> Optional[Tag]:
        if 'clas' in url:
            return soup.find("div", {"class":"entry-content"})       
        elif items := soup.find("article", {"class":"node node-directory clearfix"}):
            return items
        else:
            return soup.find("section", {"class":"col-sm-9"})
                    
    def getName(self, soup: BeautifulSoup, url: str) -> Optional[Tag]:
         if 'clas' in url:
            return soup.find("div",{'class':'name'}).getText().split(",")[0]
         else:
            return soup.find("h1",{'class':'page-header'}).getText().split(",")[0]
                    
    def scrapeURLs(self, soup: BeautifulSoup) -> ResultSet:
        return soup.select(".directory-back > a:last-of-type")
    
class History(FacultyWebScraper):

    def __init__(self):
        self.baseURL = "https://history.charlotte.edu"
        self.directoryURLs = ["https://history.charlotte.edu/people/faculty/people"]

    def getRawHtml(self, soup: BeautifulSoup, url: str) -> Optional[Tag]:
        if 'pages' in url:
            return soup.find("div", {"class":"one-sidebar-width right-sidebar"})
        else:
            return soup.find("section", {"class":"col-sm-9"})
    
    def getName(self, soup: BeautifulSoup, url: str) -> str:
        if 'pages' in url:
            return soup.find("div",{'class':'name'}).getText().split(",")[0]
        else:
            return soup.find("h1",{'class':'page-header'}).getText().split(",")[0]
        
    def scrapeURLs(self, soup: BeautifulSoup) -> ResultSet:
        return soup.find_all("a",{"class":"thumbnail-link"})
    
class Languages(FacultyWebScraper):

    def __init__(self):
        self.baseURL = "https://languages.charlotte.edu/"
        self.directoryURLs = ["https://languages.charlotte.edu/people"]

    def getRawHtml(self, soup: BeautifulSoup, url: str) -> Optional[Tag]:
        return soup.find("article", {"class": ["node node-directory clearfix", 
            "node node-directory node-promoted clearfix"]})

    def getName(self, soup: BeautifulSoup, url: str) -> Optional[Tag]:
        return soup.find("h1", {'class': 'page-header'}).getText()
    
    def scrapeURLs(self, soup: BeautifulSoup) -> ResultSet:
        return soup.find_all("a", href=True, alt=True, title=True)
    
class Mathematics(FacultyWebScraper):

    def __init__(self):
        self.baseURL = "https://math.charlotte.edu"
        self.directoryURLs = ["https://math.charlotte.edu/directory-list/faculty"]

    def getRawHtml(self, soup: BeautifulSoup, url: str) -> Optional[Tag]:
        if 'clas' in url:
            return soup.find("div", {"class":"entry-content"})       
        else:
            return soup.find("article", {"class":"node node-directory node-promoted clearfix"})
                    
    def getName(self, soup: BeautifulSoup, url: str) -> Optional[Tag]:
         if 'clas' in url:
            return soup.find("div",{'class':'name'}).getText().split(",")[0]
         else:
            return soup.find("h1",{'class':'page-header'}).getText().split(",")[0]
                    
    def scrapeURLs(self, soup: BeautifulSoup) -> ResultSet:
        return soup.find_all("a", {"class": "button button-gray"})
    
class Philosophy(FacultyWebScraper):

    def __init__(self):
        self.baseURL = "https://philosophy.charlotte.edu"
        self.directoryURLs = ["https://philosophy.charlotte.edu/directory-list/faculty"]

    def getRawHtml(self, soup: BeautifulSoup, url: str) -> Optional[Tag]:
        if 'pages' in url:
            return soup.find("div", {"class":"one-sidebar-width right-sidebar"})
        else:
            return soup.find("div", {"class":"col-sm-9"})
                    
    def getName(self, soup: BeautifulSoup, url: str) -> Optional[Tag]:
         if 'pages' in url:
            return soup.find("div",{'class':'page-title'}).getText().split(",")[0]
         else:
            return soup.find("h1",{'class':'page-header'}).getText().split(",")[0]
                    
    def scrapeURLs(self, soup: BeautifulSoup) -> ResultSet:
        return soup.find_all("a", {"class": "button button-gray"})#]
    
class Physics(FacultyWebScraper):

    def __init__(self):
        self.baseURL = "https://physics.charlotte.edu/"
        self.directoryURLs = ["https://physics.charlotte.edu/people"]

    def getRawHtml(self, soup: BeautifulSoup, url: str) -> Optional[Tag]:
        return soup.find("article", {"class": "node node-directory node-promoted clearfix"})

    def getName(self, soup: BeautifulSoup, url: str) -> Optional[Tag]:
        return soup.find("h1", {'class':'page-header'}).getText()
    
    def scrapeURLs(self, soup: BeautifulSoup) -> ResultSet:
        return soup.find_all("a", href=True, alt=True, title=True)
    
class PoliticalScience(FacultyWebScraper):

    def __init__(self):
        self.baseURL = "https://politicalscience.charlotte.edu/"
        self.directoryURLs = ["https://politicalscience.charlotte.edu/directory-list/full-time-faculty"]

    def getRawHtml(self, soup: BeautifulSoup, url: str) -> Optional[Tag]:
        if 'clas' in url:
            return soup.find("div", {"class":"entry-content"})       
        else:
            return soup.find("article", {"class":"node node-directory node-promoted clearfix"})
                    
    def getName(self, soup: BeautifulSoup, url: str) -> Optional[Tag]:
         if 'clas' in url:
            return soup.find("div",{'class':'name'}).getText().split(",")[0]
         else:
            return soup.find("h1",{'class':'page-header'}).getText().split(",")[0]
                    
    def scrapeURLs(self, soup: BeautifulSoup) -> ResultSet:
        return soup.find_all("a", {"class": "button button-gray"})
    
class PsychologicalScience(FacultyWebScraper):

    def __init__(self):
        self.baseURL = "https://psych.charlotte.edu"
        self.directoryURLs = ["https://psych.charlotte.edu/people"]

    def getRawHtml(self, soup: BeautifulSoup, url: str) -> Optional[Tag]:
        if 'clas' in url:
            return soup.find("div", {"class":"entry-content"})       
        elif items := soup.find("div", {"class":"region region-content"}):
            return items
        else:
            return soup.find("section", {"class":"col-sm-9"})
                    
    def getName(self, soup: BeautifulSoup, url: str) -> Optional[Tag]:
        if 'clas' in url:
            name = soup.find("div",{'class':'name'}).getText().split(",")[0]
        else:
            name = soup.find("h1",{'class':'page-header'}).getText()
        
        # reverse comma seperated "last, first" formatted name
        if ',' in name:
            name = name.split(",")
            name.reverse()
            name = ' '.join([string.strip() for string in name])

        return name
         
    def scrapeURLs(self, soup: BeautifulSoup) -> ResultSet:
        return soup.select(".directory-back > a:last-of-type")
    
class ReligiousStudies(FacultyWebScraper):

    def __init__(self):
        self.baseURL = "https://religiousstudies.charlotte.edu"
        self.directoryURLs = ["https://religiousstudies.charlotte.edu/directory/faculty-and-staff"]

    def getRawHtml(self, soup: BeautifulSoup, url: str) -> Optional[Tag]:
        if 'clas' in url:
            return soup.find("div", {"class":"entry-content"})       
        elif items := soup.find("section", {"class":"col-sm-9"}):
            return items
        else:
            return soup.find("article", {"class":"node node-directory node-promoted clearfix"})
                    
    def getName(self, soup: BeautifulSoup, url: str) -> Optional[Tag]:
         if 'clas' in url:
            return soup.find("div",{'class':'name'}).getText().split(",")[0]
         else:
            return soup.find("h1",{'class':'page-header'}).getText().split(",")[0]
                    
    def scrapeURLs(self, soup: BeautifulSoup) -> ResultSet:
        return soup.select(".directory-back > a:last-of-type")

class Sociology(FacultyWebScraper):

    def __init__(self):
        self.baseURL = "https://sociology.charlotte.edu"
        self.directoryURLs = ["https://sociology.charlotte.edu/directory-list/full-time-faculty"]

    def getRawHtml(self, soup: BeautifulSoup, url: str) -> Optional[Tag]:
        if 'clas' in url:
            return soup.find("div", {"class":"entry-content"})       
        else:
            return soup.find("article", {"class":"node node-directory node-promoted clearfix"})
                    
    def getName(self, soup: BeautifulSoup, url: str) -> Optional[Tag]:
         if 'clas' in url:
            return soup.find("div",{'class':'name'}).getText().split(",")[0]
         else:
            return soup.find("h1",{'class':'page-header'}).getText().split(",")[0]
                    
    def scrapeURLs(self, soup: BeautifulSoup) -> ResultSet:
        return soup.find_all("a", {"class": "button button-gray"})
    
class Writing(FacultyWebScraper):

    def __init__(self):
        self.baseURL = "https://writing.charlotte.edu"
        self.directoryURLs = ["https://writing.charlotte.edu/directory-grid/faculty"]

    def getRawHtml(self, soup: BeautifulSoup, url: str) -> Optional[Tag]:
        if 'clas' in url:
            return soup.find("div", {"class":"entry-content"})       
        else:
            return soup.find("section", {"class":"col-sm-9"})
                    
    def getName(self, soup: BeautifulSoup, url: str) -> Optional[Tag]:
         if 'clas' in url:
            return soup.find("div",{'class':'name'}).getText().split(",")[0]
         else:
            return soup.find("h1",{'class':'page-header'}).getText().split(",")[0]
                    
    def scrapeURLs(self, soup: BeautifulSoup) -> ResultSet:
        return soup.find_all("a",{"class":"thumbnail-link"})
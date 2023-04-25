
from bs4 import BeautifulSoup, ResultSet, Tag
from typing import Optional
from .FacultyWebScraper import FacultyWebScraper

class AfricanaStudies(FacultyWebScraper):

    def run(self):
        print("Starting Africana Studies Lib Science")
        baseURL = "https://africana.charlotte.edu"
        directoryURL = "https://africana.charlotte.edu/people/full-time-faculty"

        self.facultyURLs = self.getFacultyURLs(baseURL, directoryURL)
        self.profiles = self.getProfilePage(self.facultyURLs)

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

    def run(self):
        print("Starting Antropology Lib Science")
        baseURL = "https://anthropology.charlotte.edu"
        directoryURL = "https://anthropology.charlotte.edu/people"
        
        self.facultyURLs = self.getFacultyURLs(baseURL, directoryURL)
        self.profiles = self.getProfilePage(self.facultyURLs)

    def getRawHtml(self, soup: BeautifulSoup, url: str) -> Optional[Tag]:
        return soup.find("article", {"class": "node node-directory node-promoted clearfix"})

    def getName(self, soup: BeautifulSoup, url: str) -> Optional[Tag]:
        return soup.find("h1",{'class':'page-header'}).getText().split(",")[0]
    
    def scrapeURLs(self, soup: BeautifulSoup) -> ResultSet:
        return soup.select(".directory-back > a:last-of-type")
    
class BiologicalSciences(FacultyWebScraper):

    def run(self):
        print("Starting Biological Lib Science")
        baseURL = "https://biology.charlotte.edu"
        directoryURL = "https://biology.charlotte.edu/directory/faculty"

        self.facultyURLs = self.getFacultyURLs(baseURL, directoryURL)
        self.profiles = self.getProfilePage(self.facultyURLs)

    def getRawHtml(self, soup: BeautifulSoup, url: str) -> Optional[Tag]:
        return soup.find("article", {"class": "node node-directory node-promoted clearfix"})

    def getName(self, soup: BeautifulSoup, url: str) -> Optional[Tag]:
        return soup.find("h1",{'class':'page-header'}).getText().split(",")[0]
    
    def scrapeURLs(self, soup: BeautifulSoup) -> ResultSet:
        return soup.select(".caption > a")

class Chemistry(FacultyWebScraper):

    def run(self):
        print("Starting Chemistry Lib Science")
        baseURL = "https://chemistry.charlotte.edu"
        directoryURL = "https://chemistry.charlotte.edu/directory-grid/faculty"

        self.facultyURLs = self.getFacultyURLs(baseURL, directoryURL)
        self.profiles = self.getProfilePage(self.facultyURLs)

    def getRawHtml(self, soup: BeautifulSoup, url: str) -> Optional[Tag]:
        return soup.find("article", {"class": "node node-directory node-promoted clearfix"})

    def getName(self, soup: BeautifulSoup, url: str) -> Optional[Tag]:
        return soup.find("h1",{'class':'page-header'}).getText().split(",")[0]
    
    def scrapeURLs(self, soup: BeautifulSoup) -> ResultSet:
        return soup.find_all("a",{"class":"thumbnail-link"})

class Communication(FacultyWebScraper):

    def run(self):
        print("Starting Communication Studies Lib Science")
        directoryURL = "https://communication.charlotte.edu/people/full-time-faculty"
        baseURL = "https://communication.charlotte.edu"
    
        self.facultyURLs = self.getFacultyURLs(baseURL, directoryURL)
        self.profiles = self.getProfilePage(self.facultyURLs)
        
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

    def run(self):
        print("Starting Criminal Justice Lib Science")
        directoryURL = "https://criminaljustice.charlotte.edu/people/faculty"
        baseURL = "https://criminaljustice.charlotte.edu"
        
        self.facultyURLs = self.getFacultyURLs(baseURL, directoryURL)
        self.profiles = self.getProfilePage(self.facultyURLs)

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
    
    def run(self):
        print("Starting English Lib Science")
        directoryURL = "https://english.charlotte.edu/directory-list/professorial-faculty"
        baseURL = "https://english.charlotte.edu"
    
        self.facultyURLs = self.getFacultyURLs(baseURL, directoryURL)
        self.profiles = self.getProfilePage(self.facultyURLs)
    
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
 
    def run(self):
        print("Starting Geography and Earth Studies Lib Science")
        directoryURL = "https://geoearth.charlotte.edu/directory-flip/full-time-faculty"
        baseURL = "https://geoearth.charlotte.edu"
    
        self.facultyURLs = self.getFacultyURLs(baseURL, directoryURL)
        self.profiles = self.getProfilePage(self.facultyURLs)

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

    def run(self):
        print("Starting Global Studies Lib Science")
        directoryURL = "https://globalstudies.charlotte.edu/people"
        baseURL = "https://globalstudies.charlotte.edu"
    
        self.facultyURLs = self.getFacultyURLs(baseURL, directoryURL)
        self.profiles = self.getProfilePage(self.facultyURLs)

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

    def run(self):
        print("Starting History Lib Science")
        directoryURL = "https://history.charlotte.edu/people/faculty"
        baseURL = "https://history.charlotte.edu/people/faculty"
      
        self.facultyURLs = self.getFacultyURLs(baseURL, directoryURL)
        self.profiles = self.getProfilePage(self.facultyURLs)

    def getRawHtml(self, soup: BeautifulSoup, url: str) -> Optional[Tag]:
        if 'pages' in url:
            return soup.find("div", {"class":"one-sidebar-width right-sidebar"})
        else:
            return soup.find("section", {"class":"col-sm-9"})
    
    def getName(self, soup: BeautifulSoup, url: str) -> str:
        if 'pages' in url:
            return soup.find("div",{'class':'page-title'}).getText().split(",")[0]
        else:
            return soup.find("h1",{'class':'page-header'}).getText().split(",")[0]
        
    def scrapeURLs(self, soup: BeautifulSoup) -> ResultSet:
        return soup.find_all("a",{"class":"thumbnail-link"})
    
class Languages(FacultyWebScraper):

    def run(self):
        print("Starting Languages Lib Science")
        baseURL = "https://languages.charlotte.edu/"
        directoryURL = "https://languages.charlotte.edu/people"

        self.facultyURLs = self.getFacultyURLs(baseURL, directoryURL)
        self.profiles = self.getProfilePage(self.facultyURLs)

    def getRawHtml(self, soup: BeautifulSoup, url: str) -> Optional[Tag]:
        return soup.find("article", {"class": ["node node-directory clearfix", 
            "node node-directory node-promoted clearfix"]})

    def getName(self, soup: BeautifulSoup, url: str) -> Optional[Tag]:
        return soup.find("h1", {'class': 'page-header'}).getText()
    
    def scrapeURLs(self, soup: BeautifulSoup) -> ResultSet:
        return soup.find_all("a", href=True, alt=True, title=True)
    
class Mathematics(FacultyWebScraper):

    def run(self):
        print("Starting Mathematics Lib Science")
        directoryURL = "https://math.charlotte.edu/directory-list/faculty"
        baseURL = "https://math.charlotte.edu"

        self.facultyURLs = self.getFacultyURLs(baseURL, directoryURL)
        self.profiles = self.getProfilePage(self.facultyURLs)

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

    def run(self):
        print("Starting Philosophy Lib Science")
        directoryURL = "https://philosophy.charlotte.edu/directory-list/faculty"
        baseURL = "https://philosophy.charlotte.edu"
        
        self.facultyURLs = self.getFacultyURLs(baseURL, directoryURL)
        self.profiles = self.getProfilePage(self.facultyURLs)

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

    def run(self):
        print("Starting Physics Lib Science")
        baseURL = "https://physics.charlotte.edu/"
        directoryURL = "https://physics.charlotte.edu/people"

        self.facultyURLs = self.getFacultyURLs(baseURL, directoryURL)
        self.profiles = self.getProfilePage(self.facultyURLs)

    def getRawHtml(self, soup: BeautifulSoup, url: str) -> Optional[Tag]:
        return soup.find("article", {"class": "node node-directory node-promoted clearfix"})

    def getName(self, soup: BeautifulSoup, url: str) -> Optional[Tag]:
        return soup.find("h1", {'class':'page-header'}).getText()
    
    def scrapeURLs(self, soup: BeautifulSoup) -> ResultSet:
        return soup.find_all("a", href=True, alt=True, title=True)
    
class PoliticalScience(FacultyWebScraper):

    def run(self):
        print("Starting Political Science")
        directoryURL = "https://politicalscience.charlotte.edu/directory-list/full-time-faculty"
        baseURL = "https://politicalscience.charlotte.edu/"
    
        self.facultyURLs = self.getFacultyURLs(baseURL, directoryURL)
        self.profiles = self.getProfilePage(self.facultyURLs)

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

    def run(self):
        print("Starting Global Studies Lib Science")
        directoryURL = "https://psych.charlotte.edu/people"
        baseURL = "https://psych.charlotte.edu"
    
        self.facultyURLs = self.getFacultyURLs(baseURL, directoryURL)
        self.profiles = self.getProfilePage(self.facultyURLs)

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

    def run(self):
        print("Starting Religious Studies Lib Science")
        directoryURL = "https://religiousstudies.charlotte.edu/directory/faculty-and-staff"
        baseURL = "https://religiousstudies.charlotte.edu"
    
        self.facultyURLs = self.getFacultyURLs(baseURL, directoryURL)
        self.profiles = self.getProfilePage(self.facultyURLs)

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

    def run(self):
        print("Starting Sociology Lib Science")
        directoryURL = "https://sociology.charlotte.edu/directory-list/full-time-faculty"
        baseURL = "https://sociology.charlotte.edu"
    
        self.facultyURLs = self.getFacultyURLs(baseURL, directoryURL)
        self.profiles = self.getProfilePage(self.facultyURLs)

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

    def run(self):
        print("Starting Writing Lib Science")
        directoryURL = "https://writing.charlotte.edu/directory-grid/faculty"
        baseURL = "https://writing.charlotte.edu"

        self.facultyURLs = self.getFacultyURLs(baseURL, directoryURL)
        self.profiles = self.getProfilePage(self.facultyURLs)

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
#Jacob Nyborg
import requests
from bs4 import BeautifulSoup
from Model.model import FacultyProfile
from ..FacultyWebScraper import FacultyWebScraper
class ReligiousStudies(FacultyWebScraper):

    def getProfilePage(self) -> list[FacultyProfile]:
        profiles = []
        for url in self.facultyURLs:
            try:
                page = requests.get(url)
                soup = BeautifulSoup(page.content, "lxml")
                rawHtml = ''
                name = ''
                if 'clas' in url:
                    rawHtml = soup.find("div", {"class":"entry-content"})
                    name = soup.find("div",{'class':'name'}).getText().split(",")[0]
                elif items := soup.find("section", {"class":"col-sm-9"}):
                    rawHtml = items
                    name = soup.find("h1",{'class':'page-header'}).getText().split(",")[0]
                else:
                    rawHtml = soup.find("article", {"class":"node node-directory node-promoted clearfix"})
                    name = soup.find("h1",{'class':'page-header'}).getText().split(",")[0]

                profiles.append(FacultyProfile(name=name, rawHtml=rawHtml, url=url))

            except Exception as e:
                print(f"Something went wrong when visiting {url}:")
                print(e)
        return profiles

    def __init__(self):
        print("Starting Religious Studies Lib Science")
        directoryURL = "https://religiousstudies.charlotte.edu/directory/faculty-and-staff"
        baseURL = "https://religiousstudies.charlotte.edu"
    
        html_text = requests.get(directoryURL)
        soup = BeautifulSoup(html_text.content, "lxml")

        self.facultyURLs = self.getFacultyURLs(baseURL, soup.select(".directory-back > a:last-of-type"))
        self.profiles = self.getProfilePage()

if __name__ == '__main__':
    ReligiousStudies()
#Steven wilson
import requests
from bs4 import BeautifulSoup

class Anthropology:

    def getFacultyURLs(self, baseURL, soup):
        URLs = []
        soupList = soup.select(".directory-back > a")
        
        for i in soupList:
            profURL = baseURL + i.get("href")
            URLs.append(profURL)
    
        return URLs

    def getProfilePage(self, facultyURLs):
        myList = []
        for i in facultyURLs:
            try:
                page = requests.get(i)
                soup = BeautifulSoup(page.content, "html.parser")
                items = soup.find("article", {"class":"node node-directory node-promoted clearfix"})

                profileDict = {
                    'Title': soup.find("h1",{'class':'page-header'}).getText().split(",")[0],
                    'Content': items,
                }
                myList.append(profileDict)
            except Exception:
                print("Error: Doesn't have profile page or has incompatible format")
        
        return myList
    
    def __init__(self):
        print("Starting Antropology Lib Science")
        baseURL = "https://anthropology.charlotte.edu"
        directoryURL = "https://anthropology.charlotte.edu/people"
        
        html_text = requests.get(directoryURL)
        soup = BeautifulSoup(html_text.content, "html.parser")

        self.facultyURLs = self.getFacultyURLs(baseURL, soup)
        self.profiles = self.getProfilePage(self.facultyURLs)

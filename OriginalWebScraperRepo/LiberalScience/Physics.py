#Ozzy Toth
import requests
from bs4 import BeautifulSoup

class Physics:

    def getFacultyURLs(self, baseURL, soup):
        URLs = []
        soupList = soup.find_all(
            "a", href=True, alt=True, title=True)

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
                items = soup.find(
                    "article", {"class": "node node-directory node-promoted clearfix"})

                profileDict = {
                    'Title': soup.find("h1", {'class': 'page-header'}).getText(),
                    'Content': items,
                }

                myList.append(profileDict)
            except:
                print("Error: Doesn't have profile page")

        return myList

    def __init__(self):
        print("Starting Physics Lib Science")
        baseURL = "https://physics.charlotte.edu/"
        URL = "https://physics.charlotte.edu/people"

        html_text = requests.get(URL)
        soup = BeautifulSoup(html_text.content, "html.parser")

        self.facultyURLs = self.getFacultyURLs(baseURL, soup)
        self.profiles = self.getProfilePage(self.facultyURLs)
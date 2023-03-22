import requests
from bs4 import BeautifulSoup


class Mechanical:

    def getFacultyURLs(self, baseURL, soup):
        URLs = []
        soupList = soup.find_all(
            "a", {"class": "button button-green button-small"})

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
            except Exception:
                print("Error: Doesn't have profile page")

        return myList

    def __init__(self):
        print("Starting Mechanical Engineering")
        baseURL = "https://mees.charlotte.edu/"

        #Main directory
        URL = "https://mees.charlotte.edu/directory/faculty"
        #Emeritus
        URLemeritus = 'https://mees.charlotte.edu/directory-box/professors-emeriti'
        #Staff directory - don't know if this is needed
        URLstaff = 'https://mees.charlotte.edu/directory/staff'

        #Main directory
        html_text = requests.get(URL)
        soup = BeautifulSoup(html_text.content, "html.parser")

        #Emeritus
        html_text = requests.get(URLemeritus)
        soup_Emeritus = BeautifulSoup(html_text.content, "html.parser")

        #Staff directory 
        html_text = requests.get(URLstaff)
        soup_Staff = BeautifulSoup(html_text.content, "html.parser")

        self.facultyURLs = self.getFacultyURLs(baseURL, soup)
        self.profiles = self.getProfilePage(self.facultyURLs)

        self.emeritusURLs = self.getFacultyURLs(baseURL, soup_Emeritus)
        self.emeritusProfiles = self.getProfilePage(self.emeritusURLs)

        self.staffURLs = self.getFacultyURLs(baseURL, soup_Staff)
        self.staffProfiles = self.getProfilePage(self.staffURLs)

        self.facultyURLs += self.emeritusURLs
        self.facultyURLs += self.staffURLs

        self.profiles += self.emeritusProfiles
        self.profiles += self.staffProfiles

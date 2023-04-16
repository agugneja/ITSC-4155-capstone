import requests
from bs4 import BeautifulSoup

class Electrical:

    def getFacultyURLs(self, baseURL: str, soup: BeautifulSoup) -> list[str]:
        URLs = []
        soupList = soup.find_all(
            "a", {"class": "button button-green button-small"})
        
        for a_tag in soupList:
            href = a_tag.get("href")
            profURL = baseURL + href if href.startswith('/') else href
            URLs.append(profURL)
        
        return URLs
    

    def getProfilePage(self, facultyURLs):
        bad_urls = []
        profiles = []
        for url in facultyURLs:
            try:
                page = requests.get(url)
                soup = BeautifulSoup(page.content, "lxml")
                items = soup.find(
                    "article", {"class": "node node-directory node-promoted clearfix"})

                profileDict = {
                    'Title': soup.find("h1", {'class': 'page-header'}).getText(),
                    'Content': items,
                }
                profiles.append(profileDict)
            except Exception as e:
                print(f"Something went wrong when visiting {url}:")
                print(e)
                bad_urls.append(url)
        self.facultyURLs = [url for url in self.facultyURLs if url not in bad_urls]

        return profiles

    def __init__(self):
        print("Starting Electrical Engineering")
        baseURL = "https://ece.charlotte.edu"

        #Main directory
        URL = "https://ece.charlotte.edu/directory/faculty"
        #Emeritus
        URLemeritus = 'https://ece.charlotte.edu/directory/professors-emeriti'
        #Staff directory - don't know if this is needed
        URLstaff = 'https://ece.charlotte.edu/directory/staff'

        #Main directory
        html_text = requests.get(URL)
        soup = BeautifulSoup(html_text.content, "lxml")

        #Emeritus
        html_text = requests.get(URLemeritus)
        soup_Emeritus = BeautifulSoup(html_text.content, "lxml")

        #Staff directory 
        html_text = requests.get(URLstaff)
        soup_Staff = BeautifulSoup(html_text.content, "lxml")

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
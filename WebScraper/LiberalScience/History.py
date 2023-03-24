# Jacob Nyborg
import requests
from bs4 import BeautifulSoup

class History:

    #This page has the full url not extensions
    def getFacultyURLs(self, soup, baseURL):
        URLs = []
        soupList = soup.find_all("a",{"class":"thumbnail-link"})
        
        for i in soupList:
            if 'pages' in i.get("href"):
                URLs.append(i.get("href"))
            else:
                profURL = baseURL + i.get("href")
                URLs.append(profURL)
        
        return URLs

    def getProfilePage(self, facultyURLs):
        myList = []
        for i in facultyURLs:
            try:
                page = requests.get(i)
                soup = BeautifulSoup(page.content, "html.parser")
                
                if 'pages' in i:
                    items = soup.find("div", {"class":"one-sidebar-width right-sidebar"})
                    profileDict = {
                        'Title': soup.find("div",{'class':'page-title'}).getText().split(",")[0],
                        'Content': items,
                    }

                else:
                    items = soup.find("div", {"class":"col-sm-9"})
                    profileDict = {
                        'Title': soup.find("h1",{'class':'page-header'}).getText().split(",")[0],
                        'Content': items,
                    }   

                myList.append(profileDict)

            except Exception:
                print("Error: Doesn't have profile page or has incompatible format")
                print(i)
        
        return myList

    def __init__(self):
        print("Starting History Lib Science")
        directoryURL = "https://history.charlotte.edu/people/faculty"
        baseURL = "https://history.charlotte.edu/people/faculty"
        
        html_text = requests.get(directoryURL)
        soup = BeautifulSoup(html_text.content, "html.parser")

        self.facultyURLs = self.getFacultyURLs(soup, baseURL)
        self.profiles = self.getProfilePage(self.facultyURLs)
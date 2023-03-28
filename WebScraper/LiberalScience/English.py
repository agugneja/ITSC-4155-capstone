#Jacob Nyborg
import requests
from bs4 import BeautifulSoup

class English:

    #This page has the full url not extensions
    def getFacultyURLs(self, soup, baseURL):
        URLs = []
        soupList = soup.find_all("a",{"class":"button button-gray"})
        
        for i in soupList:
            if 'clas' in i.get("href"):
                URLs.append(i.get("href"))
            else:
                profURL = baseURL + i.get("href")
                URLs.append(profURL)
        
        return URLs

    #This directory has 2 main variants so this should check for both
    def getProfilePage(self, facultyURLs):
        myList = []
        for i in facultyURLs:
            try:
                page = requests.get(i)
                soup = BeautifulSoup(page.content, "html.parser")
                
                if 'clas' in i:
                    items = soup.find("div", {"class":"entry-content"})
                    profileDict = {
                        'Title': soup.find("div",{'class':'name'}).getText().split(",")[0],
                        'Content': items,
                    }

                else:
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
        print("Starting English Lib Science")
        directoryURL = "https://english.charlotte.edu/directory-list/professorial-faculty"
        baseURL = "https://english.charlotte.edu"
    
        html_text = requests.get(directoryURL)
        soup = BeautifulSoup(html_text.content, "html.parser")

        self.facultyURLs = self.getFacultyURLs(soup, baseURL)
        self.profiles = self.getProfilePage(self.facultyURLs)
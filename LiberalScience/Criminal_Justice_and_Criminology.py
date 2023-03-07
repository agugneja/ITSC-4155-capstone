#Steven wilson/ Jacob Nyborg
import requests
from bs4 import BeautifulSoup

class Criminal_Justice_and_Criminology:

    #This page has the full url not extensions
    def getFacultyURLs(self, soup, baseURL):
        URLs = []
        soupList = soup.find_all("a",{"class":"button button-gray"})
        
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
                    items = soup.find("div", {"id":"content_pane"})
                    profileDict = {
                        'Title': soup.find("div",{'class':'name'}).getText().split(",")[0],
                        'Content': items,
                    }

                else:
                    items = soup.find("div", {"class":"col-sm-9"})
                    profileDict = {
                        'Title': soup.find("h1",{'class':'page-header'}).getText().split(",")[0],
                        'Content': items,
                    }   

                myList.append(profileDict)

            except:
                print("Error: Doesn't have profile page or has incompatible format")
        
        return myList

    def __init__(self):
        print("Starting Criminal Justice Lib Science")
        directoryURL = "https://criminaljustice.charlotte.edu/people/faculty"
        baseURL = "https://criminaljustice.charlotte.edu"
        
        html_text = requests.get(directoryURL)
        soup = BeautifulSoup(html_text.content, "html.parser")

        self.facultyURLs = self.getFacultyURLs(soup, baseURL)
        self.profiles = self.getProfilePage(self.facultyURLs)

#Jacob Nyborg
import requests
from bs4 import BeautifulSoup

class PsychologicalSciences:

    #This page has the full url not extensions
    def getFacultyURLs(self, soup, baseURL):
        URLs = []
        soupList = soup.find_all("div",{"class":"directory-back"})
        
        for i in soupList:
            text = str(i)
            try:
                text = text.split("href=")[2].split(" ")[0].replace('"', '')
            except:
                text = text.split("href=")[1].split(" ")[0].replace('"', '')
            if 'pages' in text:
                URLs.append(text)
            else:
                profURL = baseURL + text
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
                    items = soup.find("div", {"class":"region region-content"})
                    if items:
                        profileDict = {
                        'Title': soup.find("h1",{'class':'page-header'}).getText().split(",")[0],
                        'Content': items,
                        }
                    else:
                        print("in none")
                        items = soup.find("section", {"class":"col-sm-9"})
                        profileDict = {
                        'Title': soup.find("h1",{'class':'page-header'}).getText().split(",")[0],
                        'Content': items,
                        }   

                myList.append(profileDict)

            except:
                print("Error: Doesn't have profile page or has incompatible format: " + i)
        
        return myList

    def __init__(self):
        print("Starting Global Studies Lib Science")
        directoryURL = "https://psych.charlotte.edu/people"
        baseURL = "https://psych.charlotte.edu"
    
        html_text = requests.get(directoryURL)
        soup = BeautifulSoup(html_text.content, "html.parser")

        self.facultyURLs = self.getFacultyURLs(soup, baseURL)
        self.profiles = self.getProfilePage(self.facultyURLs)
#Jacob Nyborg
import requests
from bs4 import BeautifulSoup

class Geography:

    def getFacultyURLs(self, baseURL, soup):
        URLs = []
        soupList = soup.find_all("div",{"class":"directory-back"})
        
        for div in soupList:
            a_tag = div.find_all("a")[-1]
            href = a_tag.get("href")
            profURL = baseURL + href if href.startswith('/') else href
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
                    items = soup.find("article", {"class":"node node-directory clearfix"})
                    if items:
                        profileDict = {
                        'Title': soup.find("h1",{'class':'page-header'}).getText().split(",")[0],
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
                print(i)
        
        return myList

    def __init__(self):
        print("Starting Geography and Earth Studies Lib Science")
        directoryURL = "https://geoearth.charlotte.edu/directory-flip/full-time-faculty"
        baseURL = "https://geoearth.charlotte.edu"
    
        html_text = requests.get(directoryURL)
        soup = BeautifulSoup(html_text.content, "html.parser")

        self.facultyURLs = self.getFacultyURLs(baseURL, soup)
        self.profiles = self.getProfilePage(self.facultyURLs)
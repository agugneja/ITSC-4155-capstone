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
        bad_urls = []
        profiles = []
        for url in facultyURLs:
            try:
                page = requests.get(url)
                soup = BeautifulSoup(page.content, "html.parser")
                
                if 'clas' in url:
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

                profiles.append(profileDict)

            except Exception as e:
                print(f"Something went wrong when visiting {url}:")
                print(e)
                bad_urls.append(url)
        self.facultyURLs = [url for url in self.facultyURLs if url not in bad_urls]
        
        return profiles

    def __init__(self):
        print("Starting Geography and Earth Studies Lib Science")
        directoryURL = "https://geoearth.charlotte.edu/directory-flip/full-time-faculty"
        baseURL = "https://geoearth.charlotte.edu"
    
        html_text = requests.get(directoryURL)
        soup = BeautifulSoup(html_text.content, "html.parser")

        self.facultyURLs = self.getFacultyURLs(baseURL, soup)
        self.profiles = self.getProfilePage(self.facultyURLs)
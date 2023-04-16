#Jacob Nyborg
import requests
from bs4 import BeautifulSoup

class Communication:

    #This page has the full url not extensions
    def getFacultyURLs(self, baseURL, soup):
        URLs = []
        soupList = soup.find_all(
            "a", {"class": "button button-gray"})
        
        for a_tag in soupList:
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
                soup = BeautifulSoup(page.content, "lxml")
                
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
                        items = soup.find("section", {"class":"col-sm-9"})
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
        print("Starting Communication Studies Lib Science")
        directoryURL = "https://communication.charlotte.edu/people/full-time-faculty"
        baseURL = "https://communication.charlotte.edu"
    
        html_text = requests.get(directoryURL)
        soup = BeautifulSoup(html_text.content, "lxml")

        self.facultyURLs = self.getFacultyURLs(baseURL, soup)
        self.profiles = self.getProfilePage(self.facultyURLs)
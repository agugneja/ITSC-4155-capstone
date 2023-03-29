#Steven wilson
import requests
from bs4 import BeautifulSoup
class PublicHealthSciences:

    def getFacultyURLs(self, baseURL, soup):
        URLs = []
        soupList = soup.find_all("a",{"class":"thumbnail-link"})
        
        for i in soupList:
            profURL = baseURL + i.get("href")
            URLs.append(profURL)
        
        return URLs

    def getFacultyURLsEmeritus(self, baseURL, soup):
        URLs = []
        soupList = soup.find_all("a",{"class":"button button-green"})
        
        for i in soupList:
            profURL = baseURL + i.get("href")
            URLs.append(profURL)
        
        return URLs

    def getProfilePage(self, facultyURLs):
        bad_urls = []
        myList = []
        for i in facultyURLs:
            try:
                page = requests.get(i)
                soup = BeautifulSoup(page.content, "html.parser")
                items = soup.find("article", {"class":"node node-directory node-promoted clearfix"})
                profileDict = {
                    'Title': soup.find("h1",{'class':'page-header'}).getText().split(",")[0],
                    'Content': items,
                }
                myList.append(profileDict)
            except Exception:
                print("Error: Doesn't have profile page or has incompatible format")
                bad_urls.append(i)
        self.facultyURLs = [url for url in self.facultyURLs if url not in bad_urls]
        return myList

    def __init__(self):
        print("Starting Health Sciences CHSS")
        baseURL = "https://publichealth.charlotte.edu"
        directoryURL = "https://publichealth.charlotte.edu/directory/3"
        #Second directory is for Faculty Emeriti
        directoryURLEmeritus = "https://publichealth.charlotte.edu/about%20us/emeritus-faculty"    
        
        html_text = requests.get(directoryURL)
        soup = BeautifulSoup(html_text.content, "html.parser")

        self.facultyURLs = self.getFacultyURLs(baseURL, soup)
        self.profiles = self.getProfilePage(self.facultyURLs)
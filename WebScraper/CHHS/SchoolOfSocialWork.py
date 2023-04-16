#Steven wilson
import requests
from bs4 import BeautifulSoup

class SchoolOfSocialWork:

    def getFacultyURLs(self, baseURL, soup):
        URLs = []
        soupList = soup.find_all("a",{"class":"button button-green"})
        
        for a_tag in soupList:
            href = a_tag.get("href")
            profURL = baseURL + href if href.startswith('/') else href
            URLs.append(profURL)
        
        return URLs

    def getProfilePage(self):
        bad_urls = []
        profiles = []
        for url in self.facultyURLs:
            try:
                page = requests.get(url)
                soup = BeautifulSoup(page.content, "lxml")
                items = soup.find("article", {"class":"node node-directory node-promoted clearfix"})
                
                profileDict = {
                    #The split at the end of getText() is to only get the facualty 
                    #   memebers name even when there is more information after their 
                    #   name such as their level of education
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
        print("Starting Social Work CHHS")
        baseURL = "https://socialwork.charlotte.edu"
        directoryURL = "https://socialwork.charlotte.edu/about-us/faculty-and-staff-directory"

        html_text = requests.get(directoryURL)
        soup = BeautifulSoup(html_text.content, "lxml")

        self.facultyURLs = self.getFacultyURLs(baseURL, soup)
        self.profiles = self.getProfilePage()
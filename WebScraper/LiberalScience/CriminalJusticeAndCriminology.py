#Steven wilson/ Jacob Nyborg
import requests
from bs4 import BeautifulSoup

class CriminalJusticeAndCriminology:

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

    def getProfilePage(self, facultyURLs):
        bad_urls = []
        profiles = []
        for url in facultyURLs:
            try:
                page = requests.get(url)
                soup = BeautifulSoup(page.content, "html.parser")
                
                if 'pages' in url:
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

                profiles.append(profileDict)

            except Exception as e:
                print(f"Something went wrong when visiting {url}:")
                print(e)
                bad_urls.append(url)
        self.facultyURLs = [url for url in self.facultyURLs if url not in bad_urls]
        
        return profiles

    def __init__(self):
        print("Starting Criminal Justice Lib Science")
        directoryURL = "https://criminaljustice.charlotte.edu/people/faculty"
        baseURL = "https://criminaljustice.charlotte.edu"
        
        html_text = requests.get(directoryURL)
        soup = BeautifulSoup(html_text.content, "html.parser")

        self.facultyURLs = self.getFacultyURLs(baseURL, soup)
        self.profiles = self.getProfilePage(self.facultyURLs)

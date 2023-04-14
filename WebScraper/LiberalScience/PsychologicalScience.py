#Jacob Nyborg
import requests
from bs4 import BeautifulSoup

class PsychologicalScience:

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
                    title = soup.find("div",{'class':'name'}).getText()
                    # Reverse comma delineated name
                    if ',' in title:
                        title = title.split(",")
                        title.reverse()
                        title = ' '.join([string.strip() for string in title])
                    profileDict = {
                        'Title': soup.find("div",{'class':'name'}).getText().split(",")[0],
                        'Content': items,
                    }

                else:
                    items = soup.find("div", {"class":"region region-content"})
                    title = soup.find("h1",{'class':'page-header'}).getText()
                    # Reverse comma delineated name
                    if ',' in title:
                        title = title.split(",")
                        title.reverse()
                        title = ' '.join([string.strip() for string in title])
                    if items:
                        profileDict = {
                        'Title': title,
                        'Content': items,
                        }
                    else:
                        print("in none")
                        items = soup.find("section", {"class":"col-sm-9"})
                        profileDict = {
                        'Title': title,
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
        print("Starting Global Studies Lib Science")
        directoryURL = "https://psych.charlotte.edu/people"
        baseURL = "https://psych.charlotte.edu"
    
        html_text = requests.get(directoryURL)
        soup = BeautifulSoup(html_text.content, "html.parser")

        self.facultyURLs = self.getFacultyURLs(baseURL, soup)
        self.profiles = self.getProfilePage(self.facultyURLs)
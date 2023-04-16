import requests
from bs4 import BeautifulSoup

class Motorsports:

    def getFacultyURLs(self, baseURL: str, soup: BeautifulSoup) -> list[str]:
        URLs = []
        soupList = soup.find_all(
            "a", {"class": "button button-green button-small"})
        
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
                soup = BeautifulSoup(page.content, "lxml")
                items = soup.find(
                    "article", {"class": "node node-directory node-promoted clearfix"})

                profileDict = {
                    'Title': soup.find("h1", {'class': 'page-header'}).getText(),
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
        print("Starting Motorsports Engineering")
        baseURL = "https://motorsports.charlotte.edu"
        URL = "https://motorsports.charlotte.edu/directory-box"

        html_text = requests.get(URL)
        soup = BeautifulSoup(html_text.content, "lxml")

        self.facultyURLs = self.getFacultyURLs(baseURL, soup)
        self.profiles = self.getProfilePage(self.facultyURLs)
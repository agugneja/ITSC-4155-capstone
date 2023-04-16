#Steven wilson
import requests
from bs4 import BeautifulSoup

class SchoolAndCommunityPartnerships:

    def getFacultyURLs(self, baseURL, soup):
        URLs = []
        soupList = soup.select(".directory-back > a")
        
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
                items = soup.find("article", {"class":"node node-directory clearfix"})
                
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
        print("Starting Community Education")
        baseURL = "https://osacp.charlotte.edu"
        directoryURL = "https://osacp.charlotte.edu/directory-flip"
        
        html_text = requests.get(directoryURL)
        soup = BeautifulSoup(html_text.content, "lxml")

        self.facultyURLs = self.getFacultyURLs(baseURL, soup)
        self.profiles = self.getProfilePage(self.facultyURLs)



'''
def getFacultyURLs(baseURL, soup):
        URLs = []
        soupList = soup.select(".directory-back > a")
        
        for i in soupList:
            profURL = baseURL + i.get("href")
            URLs.append(profURL)
        
        return URLs

def getProfilePage(facultyURLs):
    myList = []
    for i in facultyURLs:
        try:
            page = requests.get(i)
            soup = BeautifulSoup(page.content, "lxml")
            items = soup.find_all("article", {"class":"node node-directory clearfix"})
            
            for count, element in enumerate(items):
                items[count] = element.getText()
            
            profileDict = {
                'Title': soup.find("h1",{'class':'page-header'}).getText().split(",")[0],
                'Content': items,
            }
            myList.append(profileDict)
        except Exception:Exception:
            print("Error: Doesn't have profile page or has incompatible format")
    
    return myList


def main():
    baseURL = "https://osacp.charlotte.edu"
    directoryURL = "https://osacp.charlotte.edu/directory-flip"
    
    html_text = requests.get(directoryURL)
    soup = BeautifulSoup(html_text.content, "lxml")

    facultyURLs = getFacultyURLs(baseURL, soup)
    print(facultyURLs)

    profiles = getProfilePage(facultyURLs)
    for i in profiles:
        print(i, '\n')

    print("Num URLs: ", len(facultyURLs))    
    print("Num Profiles: ", len(profiles))


if __name__ == "__main__":
    main()
'''
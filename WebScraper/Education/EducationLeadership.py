#Steven wilson
import requests
from bs4 import BeautifulSoup

class EducationLeadership:

    def getFacultyURLs(self, baseURL, soup):
        URLs = []
        soupList = soup.find_all("a",{"class":"button button-gray"})
        
        for i in soupList:
            profURL = baseURL + i.get("href")
            URLs.append(profURL)
        
        return URLs

    def getProfilePage(self, facultyURLs):
        myList = []
        for i in facultyURLs:
            try:
                page = requests.get(i)
                soup = BeautifulSoup(page.content, "html.parser")
                items = soup.find("article", {"class":"node node-directory clearfix"})
                
                profileDict = {
                    'Title': soup.find("h1",{'class':'page-header'}).getText().split(",")[0],
                    'Content': items,
                }
                myList.append(profileDict)
            except Exception:
                print("Error: Doesn't have profile page or has incompatible format")
        
        return myList

    def __init__(self):
        print("Starting Leadership Education")
        baseURL = "https://edld.charlotte.edu"
        directoryURL = "https://edld.charlotte.edu/directory-list"
        
        html_text = requests.get(directoryURL)
        soup = BeautifulSoup(html_text.content, "html.parser")

        self.facultyURLs = self.getFacultyURLs(baseURL, soup)
        self.profiles = self.getProfilePage(self.facultyURLs)


'''
def getFacultyURLs(baseURL, soup):
        URLs = []
        soupList = soup.find_all("a",{"class":"button button-gray"})
        
        for i in soupList:
            profURL = baseURL + i.get("href")
            URLs.append(profURL)
        
        return URLs

def getProfilePage(facultyURLs):
    myList = []
    for i in facultyURLs:
        try:
            page = requests.get(i)
            soup = BeautifulSoup(page.content, "html.parser")
            items = soup.find_all("article", {"class":"node node-directory clearfix"})
            
            for count, element in enumerate(items):
                items[count] = element.getText()
            
            profileDict = {
                'Title': soup.find("h1",{'class':'page-header'}).getText().split(",")[0],
                'Content': items,
            }
            myList.append(profileDict)
        except Exception:
            print("Error: Doesn't have profile page or has incompatible format")
    
    return myList


def main():
    baseURL = "https://edld.charlotte.edu"
    directoryURL = "https://edld.charlotte.edu/directory-list"
    
    html_text = requests.get(directoryURL)
    soup = BeautifulSoup(html_text.content, "html.parser")

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
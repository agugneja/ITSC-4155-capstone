import requests
from bs4 import BeautifulSoup
from Model.model import FacultyProfile

class DataScience:
    def __init__(self):
        print("data science Started")
        baseURL = "https://datascience.charlotte.edu"
        directoryURL = "https://datascience.charlotte.edu/directory/faculty"
        html_text = requests.get(directoryURL)
        soup = BeautifulSoup(html_text.content, "lxml")
        self.facultyURLs = self.getFacultyURLs(baseURL, soup)
        self.profiles = self.getProfilePage()

    def getFacultyURLs(self, baseURL: str, soup: BeautifulSoup) -> list[str]:
        URLs = []
        soupList = soup.find_all("a",{"class":"thumbnail-link"})
        
        for a_tag in soupList:
            href = a_tag.get("href")
            profURL = baseURL + href if href.startswith('/') else href
            URLs.append(profURL)
        
        return URLs
    def getProfilePage(self) -> list[FacultyProfile]:
        profiles = []
        for url in self.facultyURLs:
            try:
                page = requests.get(url)
                soup = BeautifulSoup(page.content, "lxml")

                rawHtml = soup.find("article", {"class":"node node-directory node-promoted clearfix"})
                name = soup.find("h1",{'class':'page-header'}).getText()

                profiles.append(FacultyProfile(name=name, rawHtml=rawHtml, url=url))
            except Exception as e:
                print(f"Something went wrong when visiting {url}:")
                print(e)
        return profiles

# def getFacultyURLs(baseURL, soup):
#     URLs = []
#     soupList = soup.find_all("a",{"class":"thumbnail-link"})
    
#     for i in soupList:
#         profURL = baseURL + i.get("href")
#         URLs.append(profURL)
     
#     return URLs

# def getProfilePage(facultyURLs):
#     myList = []
#     for i in facultyURLs:
#         try:
#             page = requests.get(i)
#             soup = BeautifulSoup(page.content, "lxml")
#             # items = soup.find_all("div", {"class":"field-items"})
#             items = soup.find("article",{'class':'node node-directory node-promoted clearfix'} )
#             # for count, element in enumerate(items):
#             #     # items[count] = element.getText()
#             #     items[count] = element
            
#             profileDict = {
#                 'Title': soup.find("h1",{'class':'page-header'}).getText(),
#                 'Content': items,
#             }
#             myList.append(profileDict)
#         except Exception:
#             print("Error: Doesn't have profile page")
    
#     return myList

# if __name__ == '__main__':
    
#     baseURL = "https://datascience.charlotte.edu"
#     URL = "https://datascience.charlotte.edu/directory/faculty"

#     html_text = requests.get(URL)
#     soup = BeautifulSoup(html_text.content, "lxml")
    
#     facutlyURLs = getFacultyURLs(baseURL, soup)
#     print(facutlyURLs)
#     # print(len(facutlyURLs))
    
#     profiles = getProfilePage(facutlyURLs)
#     for i in profiles:
#         print(i, '\n')

#     print("Num URLs: ", len(facutlyURLs))    
#     print("Num Profiles: ", len(profiles)) #107 total profiles



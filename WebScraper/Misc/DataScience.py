import requests
from bs4 import BeautifulSoup

class DataScience:
    def __init__(self):
        print("data science Started")
        baseURL = "https://datascience.charlotte.edu"
        directoryURL = "https://datascience.charlotte.edu/directory/faculty"
        html_text = self.getSoup(directoryURL)
        soup = BeautifulSoup(html_text.content, "html.parser")
        self.facultyURLs = self.getFacultyURLs(baseURL, soup)
        self.profiles = self.getProfilePage(self.facultyURLs)

    def getSoup(self, URL):
        html_text = requests.get(URL)
        return html_text

    def getFacultyURLs(self, baseURL, soup):
        urls = []
        soupList = soup.find_all("a",{"class":"thumbnail-link"})
    
        for i in soupList:
            profURL = baseURL + i.get("href")
            urls.append(profURL)
    
        return urls

    def getProfilePage(self, facultyURLs):
        profiles = []
        for i in facultyURLs:
            try:
                page = requests.get(i)
                soup = BeautifulSoup(page.content, "html.parser")
                # items = soup.find_all("div", {"class":"field-items"})
                # items = soup.find("article",{'class':'node node-directory clearfix'})
                items = soup.find("article",{'class':'node node-directory node-promoted clearfix'})
            
                # for count, element in enumerate(items):
                #     items[count] = element.getText()
            
                profileDict = {
                    'Title': soup.find("h1",{'class':'page-header'}).getText(),
                    'Content': items,
                }
                profiles.append(profileDict)
            except Exception:
                print("Error: Doesn't have profile page")
    
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
#             soup = BeautifulSoup(page.content, "html.parser")
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
#     soup = BeautifulSoup(html_text.content, "html.parser")
    
#     facutlyURLs = getFacultyURLs(baseURL, soup)
#     print(facutlyURLs)
#     # print(len(facutlyURLs))
    
#     profiles = getProfilePage(facutlyURLs)
#     for i in profiles:
#         print(i, '\n')

#     print("Num URLs: ", len(facutlyURLs))    
#     print("Num Profiles: ", len(profiles)) #107 total profiles


import requests
from bs4 import BeautifulSoup

class Belk:
    def __init__(self):
        print("belk Started")
        baseURL = "https://belkcollege.charlotte.edu/"
        directoryURL = "https://belkcollege.charlotte.edu/directory"
        html_text = requests.get(directoryURL)
        soup = BeautifulSoup(html_text.content, "html.parser")
        self.facultyURLs = self.getFacultyURLs(baseURL, soup)
        self.profiles = self.getProfilePage(self.facultyURLs)

    def getFacultyURLs(self, baseURL, soup):
        URLs = []
        soupList = soup.find_all("a",{"class":"button-gray"})
        
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
                items = soup.find("article", {"class":"node node-directory-custom node-promoted clearfix"})

                profileDict = {
                    'Title': soup.find("h1",{'class':'page-header'}).getText(),
                    'Content': items,
                }
                profiles.append(profileDict)
            except Exception as e:
                print(f"Something went wrong when visiting {url}:")
                print(e)
                bad_urls.append(url)
        self.facultyURLs = [url for url in self.facultyURLs if url not in bad_urls]
        
        return profiles


# def getFacultyURLs(baseURL, soup):
#     URLs = []
#     soupList = soup.find_all("a",{"class":"button-gray"})
    
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
#             items = soup.find("article",{'class':'node node-directory-custom node-promoted clearfix'})
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
    
#     baseURL = "https://belkcollege.charlotte.edu/"
#     URL = "https://belkcollege.charlotte.edu/directory"

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
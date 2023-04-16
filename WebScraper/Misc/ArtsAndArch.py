import requests
from bs4 import BeautifulSoup


class ArtsAndArch:
    def __init__(self):
        print("Starting Arts and Architecture")
        baseURL = "https://coaa.charlotte.edu/"
        
        self.facultyURLs = []
        URL = "https://coaa.charlotte.edu/directory/faculty"
        html_text = requests.get(URL)
        soup1 = BeautifulSoup(html_text.content, "html.parser")
        self.facultyURLs += self.getFacultyURLs(URL, soup1)

        partURL = "https://coaa.charlotte.edu/directory/part-time-faculty"
        html_text = requests.get(partURL)
        soup2 = BeautifulSoup(html_text.content, "html.parser")
        self.facultyURLs += self.getFacultyURLs(partURL, soup2)
        
        adjuntURL = "https://coaa.charlotte.edu/directory/adjunct-faculty"
        html_text = requests.get(adjuntURL)
        soup3 = BeautifulSoup(html_text.content, "html.parser")
        self.facultyURLs += self.getFacultyURLs(adjuntURL, soup3)
        
        staffURL = "https://coaa.charlotte.edu/directory/staff"
        html_text = requests.get(staffURL)
        soup4 = BeautifulSoup(html_text.content, "html.parser")
        self.facultyURLs += self.getFacultyURLs(staffURL, soup4)
        
        emeritusURL = "https://coaa.charlotte.edu/directory/emeritus"
        html_text = requests.get(emeritusURL)
        soup5 = BeautifulSoup(html_text.content, "html.parser")
        self.facultyURLs += self.getFacultyURLs(emeritusURL, soup5)
        self.profiles = self.getProfilePage(self.facultyURLs)

    def getFacultyURLs(self, baseURL, soup):
        URLs = []
        soupList = soup.find_all("a",{"class":"thumbnail-link"})
        
        for a_tag in soupList:
            href = a_tag.get("href")
            profURL = baseURL + href if href.startswith('/') else href
            URLs.append(profURL)
        
        return URLs

    def getProfilePage(self, facultyURLs):
        myList = []
        for i in facultyURLs:
            try:
                page = requests.get(i)
                soup = BeautifulSoup(page.content, "html.parser")
                items = soup.find("article", {"class":"node node-directory node-promoted clearfix"})
            
                profileDict = {
                    'Title': soup.find("h1",{'class':'page-header'}).getText(),
                    'Content': items,
                }
                myList.append(profileDict)
            except Exception:
                print("Error: Doesn't have profile page")
    
        return myList



# def getFacultyURLs(baseURL, soup1, soup2, soup3, soup4, soup5):
#     URLs = []
#     soup1List = soup1.find_all("a",{"class":"thumbnail-link"})
#     soup2List = soup2.find_all("a",{"class":"thumbnail-link"})
#     soup3List = soup3.find_all("a",{"class":"thumbnail-link"})
#     soup4List = soup4.find_all("a",{"class":"thumbnail-link"})
#     soup5List = soup5.find_all("a",{"class":"thumbnail-link"})
    
#     for i in soup1List:
#         profURL = baseURL + i.get("href")
#         URLs.append(profURL)

#     for i in soup2List:
#         profURL = baseURL + i.get("href")
#         URLs.append(profURL)

#     for i in soup3List:
#         profURL = baseURL + i.get("href")
#         URLs.append(profURL)

#     for i in soup4List:
#         profURL = baseURL + i.get("href")
#         URLs.append(profURL)

#     for i in soup5List:
#         profURL = baseURL + i.get("href")
#         URLs.append(profURL)

#     return URLs

# def getProfilePage(facultyURLs):
#     myList = []
#     for i in facultyURLs:
#         try:
#             page = requests.get(i)
#             soup = BeautifulSoup(page.content, "html.parser")
#             items = soup.find_all("div", {"class":"field-items"})
            
#             for count, element in enumerate(items):
#                 items[count] = element.getText()
            
#             profileDict = {
#                 'Title': soup.find("h1",{'class':'page-header'}).getText(),
#                 'Content': items,
#             }
#             myList.append(profileDict)
#         except Exception:
#             print("Error: Doesn't have profile page")
    
#     return myList

# if __name__ == '__main__':
    
#     baseURL = "https://coaa.charlotte.edu/"
    
#     URL = "https://coaa.charlotte.edu/directory/faculty"
#     html_text = requests.get(URL)
#     soup1 = BeautifulSoup(html_text.content, "html.parser")


#     partURL = "https://coaa.charlotte.edu/directory/part-time-faculty"
#     html_text = requests.get(partURL)
#     soup2 = BeautifulSoup(html_text.content, "html.parser")

#     adjuntURL = "https://coaa.charlotte.edu/directory/adjunct-faculty"
#     html_text = requests.get(adjuntURL)
#     soup3 = BeautifulSoup(html_text.content, "html.parser")

#     staffURL = "https://coaa.charlotte.edu/directory/staff"
#     html_text = requests.get(staffURL)
#     soup4 = BeautifulSoup(html_text.content, "html.parser")

#     emeritusURL = "https://coaa.charlotte.edu/directory/emeritus"
#     html_text = requests.get(emeritusURL)
#     soup5 = BeautifulSoup(html_text.content, "html.parser")


#     facutlyURLs = getFacultyURLs(baseURL, soup1, soup2, soup3, soup4, soup5)


#     print(facutlyURLs)
#     print(len(facutlyURLs))
    
#     profiles = getProfilePage(facutlyURLs)
#     for i in profiles:
#         print(i, '\n')

#     print("Num URLs: ", len(facutlyURLs))    
#     print("Num Profiles: ", len(profiles)) #107 total profiles

    # ************************** Current Issues *************************************
    # ***** There are four faculty members that link to a different website *********
    # ***** Some profiles have all of their publications on them such as perez ******
    # ***** Time complexity is high and also have to wait on browser to load ********
    # ***** Too many for loops ******************************************************
    
    # page = requests.get(URL)
    # test = soup2.find_all("div",{"class":"field-item"})
    # print(test[0].find_all("p"))
    # print(test[0].getText())

    # word = "http://webpages.uncc.edu/cma/"
    # if("webpages" in word):
    #     print("yes")

    # baseURL = "https://cci.charlotte.edu"
    # URL = "https://cci.charlotte.edu/directory/faculty"
    # page = requests.get(URL)

    # soup = BeautifulSoup(page.content, "html.parser")
    
    # results = soup.find("a",{"class":"button-gray"}).get("href")

    # URL_Prof = baseURL + results

    # Prof_Page = requests.get(URL_Prof)
    # soup2 = BeautifulSoup(Prof_Page.content, "html.parser")

    # results2 = soup2.find("article",{"class":"node-directory"})

    # items = soup2.find_all("div", {"class":"field-items"})

    # major = items[1].getText()
    # print("Major: " + major)

    # jobTitle = items[2].getText()
    # print("Job Title: " + jobTitle)

    # building = items[3].getText()
    # print("Buidling: " + building)

    # phone = items[4].getText()
    # print("Phone #: " + phone)

    # email = items[5].getText()
    # print("Email: " + email)

    # website = items[6].getText()
    # print("\nWebsite: " + website)


  
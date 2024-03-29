from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select

import time

import requests
from bs4 import BeautifulSoup

class CCI:
    def __init__(self):
        print("CCI Started")
        baseURL = "https://cci.charlotte.edu"
        directoryURL = "https://cci.charlotte.edu/directory/faculty"
        html_text = self.getSoup(directoryURL)
        soup = BeautifulSoup(html_text, "html.parser")
        self.facultyURLs = self.getFacultyURLs(baseURL, soup)
        self.profilePages = self.getProfilePage(self.facultyURLs)

    def getSoup(self, siteUrl):
        options = Options()
        options.headless = True
        driver = webdriver.Chrome(options= options)

        driver.get(siteUrl)
        label = driver.find_element('id', 'edit-items-per-page')
        drop = Select(label)
        drop.select_by_visible_text('- All -')
        submit = driver.find_element('id', 'edit-submit-customized-directory-search')
        submit.click()

        time.sleep(1) # Have to let page load after selecting all

        html_text = driver.page_source
        return html_text


    def getFacultyURLs(self, baseURL, soup):
        urls = []
        soupList = soup.find_all("a",{"class":"button-gray"})
    
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
                items = soup.find("article",{'class':'node node-directory clearfix'})
            
                profileDict = {
                    'Title': soup.find("h1",{'class':'page-header'}).getText(),
                    'Content': items,
                }
                profiles.append(profileDict)
            except:
                print("Error: Doesn't have profile page")
    
        return profiles

# if __name__ == '__main__':
    
#     baseURL = "https://cci.charlotte.edu"
#     URL = "https://cci.charlotte.edu/directory/faculty"

#     options = Options()
#     options.headless = True
#     driver = webdriver.Chrome(options= options)

#     driver.get(URL)
#     label = driver.find_element('id', 'edit-items-per-page')
#     drop = Select(label)
#     drop.select_by_visible_text('- All -')
#     submit = driver.find_element('id', 'edit-submit-customized-directory-search')
#     submit.click()

#     time.sleep(1) # Have to let page load after selecting all

#     html_text = driver.page_source
#     soup = BeautifulSoup(html_text, "html.parser")
    
#     facutlyURLs = getFacultyURLs(baseURL, soup)
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


  
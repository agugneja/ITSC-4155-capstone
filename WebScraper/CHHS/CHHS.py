#Steven wilson and Jacob Nyborg
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
import time
import requests
from bs4 import BeautifulSoup


class CHHS:

    def getFacultyURLs(self, baseURL, soup):
        URLs = []
        soupList = soup.find_all("a",{"class":"button button-gray"})
        
        for i in soupList:
            profURL = baseURL + i.get("href")
            URLs.append(profURL)
        
        return URLs

    def clickItemsPerPage(self, URL):
        #This will change the page to list all memebers
        options = Options()
        options.headless = True
        driver = webdriver.Chrome(options= options)

        driver.get(URL)
        label = driver.find_element('id', 'edit-items-per-page')
        drop = Select(label)
        drop.select_by_visible_text('- All -')
        submit = driver.find_element('id', 'edit-submit-features-directory-search')
        submit.click()
        
        time.sleep(1) # Have to let page load after selecting all


        return driver.page_source

    def getProfilePage(self, facultyURLs):
        myList = []
        for i in facultyURLs:
            try:
                page = requests.get(i)
                soup = BeautifulSoup(page.content, "html.parser")
                items = soup.find("article", {"class":"node node-directory node-promoted clearfix"})
                
                profileDict = {
                    'Title': soup.find("h1",{'class':'page-header'}).getText().split(",")[0],
                    'Content': items,
                }
                myList.append(profileDict)
            except Exception:
                print("Error: Doesn't have profile page or has incompatible format")
        
        return myList

    def __init__(self):
        print("Starting CHHS")
        baseURL = "https://health.charlotte.edu"
        directoryURL = "https://health.charlotte.edu/about-college/faculty-and-staff"

        html_text = self.clickItemsPerPage(directoryURL)
        soup = BeautifulSoup(html_text, "html.parser")

        self.facultyURLs = self.getFacultyURLs(baseURL, soup)
        self.profiles = self.getProfilePage(self.facultyURLs)
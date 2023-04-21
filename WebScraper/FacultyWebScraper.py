from bs4 import BeautifulSoup
from bs4 import ResultSet
import traceback
import requests
from typing import Optional, Callable
from Model.model import FacultyProfile
from abc import ABC, abstractmethod

class FacultyWebScraper(ABC):
    """Base class for all department web scrapers
       
    ### Attributes:
        `bad_urls (list[str])`: A list of urls that an exception when attempting to fetch
        `facultyURLs (list[str])`: A list of urls that point to the faculty profiles that will be scraped
        `profiles (list[FacultyProfile])`: a list of FacultyProfile objects that represent the scraped profiles

    """
    bad_urls: list[str]
    facultyURLs: list[str]
    profiles: list[FacultyProfile]

    def getFacultyURLs(self, baseURL: str, directoryURL: str) -> list[str]:
        """Fetches URLs that point to faculty profiles

        ### Args:
            `baseURL (str)`: the base url for the site being scraped
            `directoryURL (str)`: the url for the specific page being scraped
        
        ### Returns:
            `list[str]`: a list of URLs that point to faculty profiles
        """
        URLs = []
        soup = self.getSoup(directoryURL)
        soupList = self.scrapeURLs(soup)
        for a_tag in soupList:
            href = a_tag.get("href")
            profURL = baseURL + href if href.startswith('/') else href
            URLs.append(profURL)
        
        return URLs
    
    
    def getProfilePage(self, urls: list[str]) -> list[FacultyProfile]:
        profiles = []
        for url in urls:
            if soup := self.getSoup(url):
                try:
                    rawHtml = self.getRawHtml(soup, url)
                    name = self.getName(soup, url)
                    profiles.append(FacultyProfile(name=name, rawHtml=str(rawHtml), url=url))
                except Exception as e:
                    print(f"Something went wrong when visiting {url}:")
                    print(e)

        return profiles
    
    def getSoup(self, url: str) -> Optional[BeautifulSoup]:
        """Creates a new object for a specified website

        ### Args:
            `url (str)`: The URL for the website you need a `BeautifulSoup` object for

        ### Returns:
            `Optional[BeautifulSoup]`: A new `BeautifulSoup` object for the website that the URL points to
            if no exception occurs, otherwise `None` 
        """
        try:
            html = requests.get(url).content
            return BeautifulSoup(html, "lxml")
        except Exception as e:
            print(f'An error occurred while fetching this page: {url}')
            print(e)
            # self.bad_urls.append(url)

    @abstractmethod
    def getRawHtml(soup: BeautifulSoup, url: str):
        ...
    
    @abstractmethod
    def getName(soup: BeautifulSoup, url: str):
        ...

    @abstractmethod
    def scrapeURLs(soup: BeautifulSoup):
        ...
    
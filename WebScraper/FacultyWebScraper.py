from bs4 import BeautifulSoup, Tag
from bs4 import ResultSet
import requests
from typing import Optional
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
        """Grabs the profile content and name of faculty members from their directory profile

        ### Args:
            `urls (list[str])`: the list of faculty profile urls 

        ### Returns:
            `list[FacultyProfile]`: a list of FacultyProfile objects that 
            represent the faculty members whose profiles were scraped
        """
        profiles = []
        for url in urls:
            if soup := self.getSoup(url):
                try:
                    rawHtml = self.getRawHtml(soup, url)
                    name = self.getName(soup, url)
                    profiles.append(FacultyProfile(name=name, department=self.__class__.__name__, rawHtml=rawHtml, url=url))
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
    def getRawHtml(self, soup: BeautifulSoup, url: str) -> Optional[Tag]:
        """Scrapes the profile content from a faculty profile page

        ### Args:
            `soup (BeautifulSoup)`: holds the html content of the page being scraped
            `url (str)`: the URL of the page being scraped (sometimes not used)

        ### Returns:
            `Optional[Tag]`: A `Tag` object representing the HTML tag containing the 
            content of the profile, or `None` if nothing was found
        """
        ...
    
    @abstractmethod
    def getName(self, soup: BeautifulSoup, url: str) -> Optional[Tag]:
        """Scrapes the name from a faculty profile page

        ### Args:
            soup (BeautifulSoup): holds the html content of the page being scraped
            url (str): the URL of the page being scraped (sometimes not used)

        ### Returns:
            `Optional[Tag]`: A `Tag` object representing the HTML tag containing the 
            faculty member's name, or `None` if nothing was found
        """
        ...

    @abstractmethod
    def scrapeURLs(self, soup: BeautifulSoup) -> ResultSet:
        """Scrapes the <a> tags that point to faculty profiles from a faculty directory

        ### Args:
            soup (BeautifulSoup): holds the html content of the directory being scraped
       
        ### Returns:
            `list[str]`: A list of <a> tags
        """
        ...
    
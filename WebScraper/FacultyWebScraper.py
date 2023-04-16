from bs4 import BeautifulSoup
from bs4 import ResultSet

class FacultyWebScraper:
    def getFacultyURLs(self, baseURL: str, soupList: ResultSet) -> list[str]:
        URLs = []
        
        for a_tag in soupList:
            href = a_tag.get("href")
            profURL = baseURL + href if href.startswith('/') else href
            URLs.append(profURL)
        
        return URLs
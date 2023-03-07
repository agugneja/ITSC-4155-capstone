import requests
from bs4 import BeautifulSoup

# page = requests.get("https://religiousstudies.charlotte.edu/directory/faculty-and-staff")
# soup = BeautifulSoup(page.content, "html.parser")
# souplist = soup.find_all("div",{"class":"directory-back"})
# print(len(souplist))
# for i in souplist:
#     text = str(i)
#     try:
#         text = text.split("href=")[2].split(" ")[0].replace('"', '')
#     except:
#         text = text.split("href=")[1].split(" ")[0].replace('"', '')
#     print(text)

try:
    requests.get("https://belkcollege.charlotte.edu//directory/suzanne-sevin")
except:
    print("worked")


# baseURL = "https://geoearth.charlotte.edu/"
# requests.get(text)

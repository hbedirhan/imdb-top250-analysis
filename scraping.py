from bs4 import BeautifulSoup
import requests
from csv import writer

url = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"
html = requests.get(url)
soup = BeautifulSoup(html.content, "html.parser")

list = soup.find('tbody', {"class":"lister-list"}).find_all("tr")

with open('imdb.csv', 'w', encoding='utf-8',newline='') as f:
    thewriter = writer(f)
    header = ['Title', 'Year', 'Rating']
    thewriter.writerow(header)

    for tr in list:
        title = tr.find("td",{"class":"titleColumn"}).find("a").text
        year = tr.find("td",{"class":"titleColumn"}).find("span").text.strip("()")
        rating = tr.find("td",{"class":"ratingColumn imdbRating"}).find("strong").text
        info = [title,year,rating]
        thewriter.writerow(info)

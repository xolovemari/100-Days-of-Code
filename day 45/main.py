import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response = requests.get(URL)
web_page = response.text
soup = BeautifulSoup(web_page, "html.parser")
movies = [title.getText() for title in soup.find_all(name="h3", class_="title")]

movies.reverse()

with open("day 45/movies.txt", "w", encoding="utf-8") as file:
    for title in movies:
        file.write(f"{title}\n")
import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response = requests.get(URL)
movie_webpage = response.text

soup = BeautifulSoup(movie_webpage,"html.parser")
# print (soup)
movies = soup.find_all(name="h3",class_="title")
# print(movies)
ordered = []
for movie in range(len(movies)-1, -1, -1):
    ordered.append(movies[movie].getText())
print(ordered)

with open("top100movies.txt", mode="w",encoding='utf-8') as file:
    for movie in ordered:
        file.write(f"{movie}\n")
from bs4 import BeautifulSoup
import requests

response = requests.get('https://www.timeout.com/newyork/movies/best-movies-of-all-time')
web_page = response.text

soup = BeautifulSoup(web_page, "html.parser")

# print(soup)
# movie_list = soup.find_all(name="h3", class_="jsx-2692754980")
movie_list = [tag.getText().strip() for tag in soup.find_all(name="a", class_="xs-text-charcoal decoration-none")]

with open('movies.txt', mode='w') as file:
    for movie in movie_list:
        # movie.replace(" ", " ")
        file.write(f"{movie}\n")

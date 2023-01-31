# Задание под номером 4
import requests
from bs4 import BeautifulSoup


url = 'https://www.kinoafisha.info/rating/movies/?page=0'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
data = soup.find_all('div', class_="movieList_item movieItem movieItem-rating movieItem-position")
counter = 0

print('Топ 10 фильмов:')
for item in data:

    name = item.find('a', class_="movieItem_title").text
    rating = item.find('span', class_="rating_num").text + '⭐️'

    # films.append(f'{name} {rating}')
    print(f'{name} {rating}')

    counter += 1

    if counter == 10:
        break






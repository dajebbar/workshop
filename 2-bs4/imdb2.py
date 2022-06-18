import pandas as pd
import requests
from bs4 import BeautifulSoup


url = 'https://www.imdb.com/title/tt0111161/'
resp2 = requests.get(url)
soup2 = BeautifulSoup(resp2.content, 'html.parser')
director_url = 'https://www.imdb.com'
# print(resp2.status_code)

init_tag = soup2.find('section',{'class': 'ipc-page-section ipc-page-section--baseAlt ipc-page-section--tp-none ipc-page-section--bp-xs sc-910a7330-1 iPKxCm'})
movie_time = init_tag.find('ul',{'class':'ipc-inline-list ipc-inline-list--show-dividers sc-8c396aa2-0 kqWovI baseAlt'}).find_all('li')[-1]
movie_genre = init_tag.find('ul',{'class':'ipc-inline-list ipc-inline-list--show-dividers ipc-inline-list--no-wrap baseAlt'}).find('li')
movie_director = init_tag.find('a',{'class':'ipc-metadata-list-item__list-content-item ipc-metadata-list-item__list-content-item--link'}).get_text()
movie_director_link = init_tag.find('a',{'class':'ipc-metadata-list-item__list-content-item ipc-metadata-list-item__list-content-item--link'}).get('href')
print(movie_time.get_text())
print(movie_genre.get_text())
print(movie_director)
print(director_url+movie_director_link)

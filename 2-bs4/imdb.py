import pandas as pd
import requests
from bs4 import BeautifulSoup


url = 'https://www.imdb.com/chart/top/'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
# print(response.status_code)

principal_tag = soup.find('tbody', {'class':'lister-list'}).find_all('tr')
movie_name = [tag.find('td', {'class':'titleColumn'}).find('a').get_text().strip() for tag in principal_tag]
movie_year = [tag.find('td', {'class':'titleColumn'}).find('span', {'class':'secondaryInfo'}).get_text().replace('(','').replace(')','').strip() for tag in principal_tag]
movie_rating = [tag.find('td', {'class':'ratingColumn imdbRating'}).find('strong').get_text().strip() for tag in principal_tag]
link = 'https://www.imdb.com/'
movie_link = [link+tag.find('td', {'class':'titleColumn'}).find('a').get('href') for tag in principal_tag]
# print(movie_name)
# print('-*-' * 50)
# print(movie_year)
# print(movie_rating)

movie_time =[]
movie_genre = []
for url_site in movie_link:
    resp2 = requests.get(url_site)
    soup2 = BeautifulSoup(resp2.content, 'html.parser')
    init_tag = soup2.find('section',{'class': 'ipc-page-section ipc-page-section--baseAlt ipc-page-section--tp-none ipc-page-section--bp-xs sc-910a7330-1 iPKxCm'})
    movie_time.append(init_tag.find('ul',{'class':'ipc-inline-list ipc-inline-list--show-dividers sc-8c396aa2-0 kqWovI baseAlt'}).find_all('li')[-1].get_text())
    movie_genre.append(init_tag.find('ul',{'class':'ipc-inline-list ipc-inline-list--show-dividers ipc-inline-list--no-wrap baseAlt'}).find('li').get_text())



# df = pd.DataFrame({'movies': movie_name, 'years': movie_year, 'ratings':movie_rating, 'links':movie_link})
# # print(df.sample(10))

# df.to_csv('imbd_top250.csv', index=False)


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
# print(movie_name)
# print('-*-' * 50)
# print(movie_year)
# print(movie_rating)

df = pd.DataFrame({'movies': movie_name, 'years': movie_year, 'ratings':movie_rating})
print(df.sample(10))
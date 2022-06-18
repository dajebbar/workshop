from urllib import response
import requests
from bs4 import BeautifulSoup


url = 'https://www.imdb.com/chart/top/'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
# print(response.status_code)

principal_tag = soup.find('tbody', {'class':'lister-list'}).find_all('tr')
movie_name = [tag.find('td', {'class':'titleColumn'}).find('a').get_text().strip() for tag in principal_tag]
movie_year = [tag.find('td', {'class':'titleColumn'}).find('span', {'class':'secondaryInfo'}).get_text().replace('(','').replace(')','').strip() for tag in principal_tag]

print(movie_name)
print('-*-' * 50)
print(movie_year)
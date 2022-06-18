import requests
from bs4 import BeautifulSoup


url = 'https://www.imdb.com/name/nm0001104/'
resp3 = requests.get(url)
soup3 = BeautifulSoup(resp3.content, 'html.parser')
tag_container = soup3.find_all('div', {'class':'knownfor-title-role'})[1:]
for tag in tag_container:
    print(tag.find('a').get('title'))
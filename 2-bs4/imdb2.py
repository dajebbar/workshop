import pandas as pd
import requests
from bs4 import BeautifulSoup


url = 'https://www.imdb.com/title/tt0111161/'
resp2 = requests.get(url)
soup2 = BeautifulSoup(resp2.content, 'html.parser')

# print(resp2.status_code)

init_tag = soup2.find('section',{'class': 'ipc-page-section ipc-page-section--baseAlt ipc-page-section--tp-none ipc-page-section--bp-xs sc-910a7330-1 iPKxCm'})
movie_time = init_tag.find('ul',{'class':'ipc-inline-list ipc-inline-list--show-dividers sc-8c396aa2-0 kqWovI baseAlt'}).find_all('li')[-1]
print(movie_time.get_text())

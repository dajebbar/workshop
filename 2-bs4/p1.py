import requests
from bs4 import BeautifulSoup


# HTTP Request
# store website
url = 'https://books.toscrape.com/'

# get request
response = requests.get(url)

# status code
print(response.status_code)
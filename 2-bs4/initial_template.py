import requests
from bs4 import BeautifulSoup

# HTTP Request
url = 'http://automationpractice.com/index.php?id_category=3&controller=category'
response = requests.get(url)

# print(response.status_code)

# Soup Object
soup = BeautifulSoup(response.content, 'html.parser')
print(soup)
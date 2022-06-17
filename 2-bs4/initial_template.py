import requests
from bs4 import BeautifulSoup

# HTTP Request
url = 'http://automationpractice.com/index.php?id_category=3&controller=category'
response = requests.get(url)

# print(response.status_code)

# Soup Object
soup = BeautifulSoup(response.content, 'html.parser')
# print(soup)

# Important Functions
# 1-find
# by id
contact_us = soup.find(id='contact-link').get_text().strip()
print(contact_us)

contact_us2 = soup.find(id='contact-link').find('a').get_text()
print(contact_us2)

# by class
product = soup.find(class_='ajax_block_product').find(class_='price product-price').get_text().strip()
print(product)

# 2-find_all findAll
products = soup.find_all(class_='product-name')
print(len(products))
for p in products:
    # p_ = p.find('a')
    print(p.get_text().strip())


# select_one
# select by css selector - return first element  - equivalent to find
phone = soup.select_one('.shop-phone').get_text().replace('Call us now:', '').strip()
print(phone)

contact_us3 = soup.select_one('#contact-link').get_text().strip()
print(contact_us3)

# select
# select by css selector - return list of elements  - equivalent to find_all

products_ = soup.select('.product-name')
print(len(products_))
for p in products_:
    print(p.get_text().strip())
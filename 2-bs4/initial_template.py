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


# get value of attributes vs get_text()
# find by attribute
article_name = soup.find(itemprop="name").find('a').get('title')
print('---' * 10)
print(article_name)

a_n = soup.find(itemprop="name").find('a').get_text().strip()
print(a_n)

# Siblings and Parents
# go to product N°1 and find next sibling
product_1_sibling = soup.select_one('.ajax_block_product').find_next_sibling().select_one('.product-name').get('title')
print(product_1_sibling)

# go to the last product and find the previous sibling
previous_last_product = soup.select('.ajax_block_product')[-1].find_previous_sibling().select_one('.product-name').get('title')
print(previous_last_product)

# go to the last product and find the parent
print('*-*' * 10)
last_product_parent = soup.select('.ajax_block_product')[-1].find_parent()
print(last_product_parent)

# Extract links

# single link
contact_us_link = soup.find(id='contact-link').find('a').get('href')
print('---' * 20)
print(contact_us_link)

# multiple links
links = []
products_container = soup.find_all(class_='product-image-container')
t = soup.find_all(itemprop='name')
print('---' * 20)
# print(type(products_container))
# print(type(t))

for l in products_container:
    if l.find('a') != None:
        links.append(l.find('a').get('href'))

print(links)

# Find Elements alternative Syntax
subcategory = soup.find('a', {'class': 'subcategory-name'}).get_text()
print(subcategory)

contact_us_follow = soup.find('div', {'id':'contact-link'}).get_text().strip()
print(contact_us_follow)


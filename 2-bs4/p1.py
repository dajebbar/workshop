import requests
import pandas as pd
from bs4 import BeautifulSoup


# HTTP Request
# store website
url = 'https://books.toscrape.com/'

# get request
response = requests.get(url)

# status code
# print(response.status_code)

# soup object
soup = BeautifulSoup(response.content, 'html.parser')
principal_tag = soup.find_all('article', {'class':'product_pod'})
book_img_link = [url+img.find('div', {'class':'image_container'}).find('a').get('href') for img in principal_tag]
book_title = [ttle.find('h3').find('a').get('title') for ttle in principal_tag]
book_price = [price.find('div', {'class': 'product_price'}).find('p',{'class':'price_color'}).get_text().replace('£','').strip() for price in principal_tag]
book_in_store = [stock.find('div', {'class': 'product_price'}).find('p',{'class':'instock availability'}).get_text().strip() for stock in principal_tag]

# print(book_img_link)
# print(book_title)
# print(book_price)
# print(book_in_store)
books_dict = {
    'titles': book_title,
    'books_img': book_img_link,
    'prices': book_price,
    'stock': book_in_store,

}
df = pd.DataFrame(books_dict)
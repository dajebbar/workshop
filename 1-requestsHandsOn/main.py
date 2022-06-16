import requests

response = requests.get('https://quotes.toscrape.com/')
# print(response.status_code)
# print(response.encoding)
html = response.text
for line in html.split('\n'):
    if '<span class="text" itemprop="text">' in line:
        print(line)
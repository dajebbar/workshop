import requests

response = requests.get('https://quotes.toscrape.com/')
# print(response.status_code)
# print(response.encoding)
html = response.text
tag = '<span class="text" itemprop="text">'
for line in html.split('\n'):
    if tag in line:
        print(line.replace(tag, '').replace('“', '').replace('”', '').replace('</span>', '').strip())
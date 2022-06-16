import requests

response = requests.get('https://quotes.toscrape.com/')
# print(response.status_code)
# print(response.encoding)
html = response.text
tag = '<span class="text" itemprop="text">'
with open('quotes.txt', 'a') as f:
    for line in html.split('\n'):
        if tag in line:
            line = line.replace(tag, '').replace('“', '').replace('”', '').replace('</span>', '').strip()
            f.write(line)
            f.write('\n')
    print('Done!')
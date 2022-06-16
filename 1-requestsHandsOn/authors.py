from cgitb import html
import requests

r = requests.get('https://quotes.toscrape.com/')
html = r.text

tag = '<small class="author" itemprop="author">'

with open('authors.txt', 'w') as f:
    for line in html.split('\n'):
        if tag in line:
            line = line.replace(tag, '').replace('<span>', '').replace('</small>', '')
            line = line.strip()
            f.write(line[2:])
            f.write('\n')
    print('Done!')
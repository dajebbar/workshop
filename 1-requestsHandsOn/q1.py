import csv
import requests

response = requests.get('https://quotes.toscrape.com/')
html = response.text
tag_quote = '<span class="text" itemprop="text">'
tag_author = '<small class="author" itemprop="author">'

result = []
quote_name = {}

for quote, name in html.split('\n'), html.split('\n'):
    if tag_quote in quote:
        quote = quote.replace(tag_quote, '').replace('“', '').replace('”', '').replace('</span>', '').strip()
    quote_name['quotes'] = quote
    if tag_author in name:
        name = name.replace(tag_author, '').replace('<span>', '').replace('</small>', '')
        name = name.strip()
    quote_name['author_names'] = name

    result.append(quote_name)

def write_dict(filename):
    with open(filename, 'a') as f:
        csv_writer = csv.DictWriter(f, delimiter=',', fieldnames=result[0].keys())
        csv_writer.writeheader()
        for line in result:
            csv_writer.writerow(line)
    print('done!!')


filename='quotes_dict.csv'
write_dict(filename)
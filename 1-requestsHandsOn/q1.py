import csv
import requests

response = requests.get('https://quotes.toscrape.com/')
html = response.text
tag_quote = '<span class="text" itemprop="text">'
tag_author = '<small class="author" itemprop="author">'
quote_name_dico = {}
result = []

for line in html.split('\n'):

    if tag_quote in line:
        quote = line.replace(tag_quote, '').replace('“', '').replace('”', '').replace('</span>', '').strip()
        
    if tag_author in line:
        author = line.replace(tag_author, '').replace('<span>', '').replace('</small>', '')
        author = author.strip()
        quote_name_dico['author_names'] = author[2:].strip()
        quote_name_dico['quotes'] = quote
        # print(quote_name_dico)
        result.append(quote_name_dico.copy())
        
    
# print(result)


def write_dict(filename):
    with open(filename, 'a') as f:
        csv_writer = csv.DictWriter(f, delimiter=',', fieldnames=result[0].keys())
        csv_writer.writeheader()
        for line in result:
            csv_writer.writerow(line)
    print('done!!')


filename='quotes_dict.csv'
write_dict(filename)
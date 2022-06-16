import csv
import requests

tag_title = '<h1 class="ds-text-title-s ds-font-bold ds-text-typo-title ds-mb-1">'
tag_content = '<p class="ds-text-compact-s ds-text-typo-paragraph ds-mb-2"><div>'
# tag_date_auth = '<span class="ds-text-compact-xs"><span>'
dico = {}
result = []
for i in range(1, 21):
    response = requests.get(f'https://www.espncricinfo.com/genre/superstats-706?page={i}')
    html = response.text
    for line in html.split('\n'):
        if tag_title in line:
            title = line.replace(tag_title, '').replace('</h1>', '').strip()
        
        if tag_content in line:
            content = line.replace(tag_content, '').replace('<div>', '').replace('</div>', '').replace('</p>', '')
            content = content.strip()
            dico['titles'] = title
            dico['contents'] = content
            
            result.append(dico.copy())
        
    
# print(result)


def write_dict(filename):
    with open(filename, 'a') as f:
        csv_writer = csv.DictWriter(f, delimiter=',', fieldnames=result[0].keys())
        csv_writer.writeheader()
        for line in result:
            csv_writer.writerow(line)
    print('done!!')


filename='superstats.csv'
write_dict(filename)
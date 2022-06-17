import requests
import json

for i in range(1, 21):
    url = f'https://www.espncricinfo.com/ci/content/story/data/index.json?genre=706;;page={i}'
    response = requests.get(url)
    data = response.text
    data = json.loads(data)
    with open('superstats.csv', 'a', encoding='utf-8') as f:
        for headline in data:
            _h = headline.replace(',', '')
            f.write(headline['headline'])
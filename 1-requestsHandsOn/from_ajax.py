import requests
import json

with open('news.txt', 'a', encoding='utf-8') as f:
    for i in range(1, 7):
        url = f'https://www.espncricinfo.com/ci/content/story/data/index.json?;type=7;page={i}'
        response = requests.get(url)
        data = json.loads(response.text)

        for news in data:
            f.write(news['date'] + ' | ' + news['author'] + ' | ' + news['summary'])
            f.write('\n')

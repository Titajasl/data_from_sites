from bs4 import BeautifulSoup
from data_from_sites import get_html

html = get_html('https://yandex.ru/search/?lr=10734&msid=1492162520.41607.22877.24979&text=python')

if html:
    bs = BeautifulSoup(html, 'html.parser')

    data = []

    for item in bs.find_all('li', class_='serp-item'):
        block_title = item.find('a', class_='organic__url')
        href = item.find('a', class_='path__item')
        data.append({
            'title': block_title.text,
            'link': href.get('href')
        })

    print(data)
else:
    print('Что-то не так!')
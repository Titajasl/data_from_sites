import requests

import os                       # Решение проблемы с кодировкой
os.system('chcp 65001')

def get_html(url):
    try:
        result = requests.get(url)
        result.raise_for_status()
        return result.text
    except requests.exceptions.RequestException as e:
        print(e)
        return False
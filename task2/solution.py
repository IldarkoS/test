from bs4 import BeautifulSoup
from collections import defaultdict

import csv
import requests


def get_animals_dict(URL: str) -> dict:
    animals_count = defaultdict(int)
    total_pages = 2 # Ограничение на количество страниц. Тк записей там 46 334 -> 232 страницы
    while URL and total_pages > 0:
        total_pages -= 1
        try:
            response = requests.get(URL, verify=True, timeout=3)
        except:
            raise ConnectionError("Connection lost!")
        if response.status_code != 200:
            response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        target = soup.find('div', {'class': 'mw-category mw-category-columns'})
        li_list = target.find_all('li')

        for li in li_list:
            animals_count[li.text[0]] += 1

        try:
            URL = BASE_URL + soup.find('a', string='Следующая страница')['href']
        except:
            URL = None
    
    return dict(animals_count)


def export_to_csv(result: dict, filename: str) -> None:
    with open(filename, mode='w') as csvfile:
        writer = csv.writer(csvfile)

        for letter, count in result.items():
            writer.writerow([letter, count])

    print("Succes!")

BASE_URL = "https://ru.wikipedia.org"
URL = BASE_URL + "/wiki/Категория:Животные_по_алфавиту"

result = get_animals_dict(URL=URL)
export_to_csv(result=result, filename="task2/beasts.csv") 
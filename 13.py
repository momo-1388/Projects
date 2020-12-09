import requests
from bs4 import BeautifulSoup
import re

r = requests.get('https://divar.ir/s/mashhad')

res = r.text

soup = BeautifulSoup(res, 'html.parser')

all_price = soup.find_all('div', attrs={'class': 'kt-post-card__title'})
all_name = soup.find_all('div', attrs={'class': 'kt-post-card__top-description kt-post-card-description'})
__price__name__ = zip(all_price, all_name)
for price_is, name_is in __price__name__:
    name = re.sub(r'\s+', ' ', price_is.text).strip()
    price = re.sub(r'\s+', ' ', name_is.text).strip()
    if price != 'توافقی':
        print(name, 'قيمت :%s' % price)

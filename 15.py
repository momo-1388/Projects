import requests
import bs4
import re

r = requests.get("https://emalls.ir/%D9%84%DB%8C%D8%B3%D8%AA-%D9%82%DB%8C%D9%85%D8%AA_%D9%84%D9%BE-%D8%AA%D8%A7%D9%BE~Category~40")

soup = bs4.BeautifulSoup(r.text, 'html.parser')

names = soup.find_all('a', attrs={'class': 'maintitle'})
prices = soup.find_all('div', attrs={'class': 'col-md-2 col-sm-12 col-12 item-price'})
for name in names:
    print(name.text.strip())

for price in prices:
    price = re.findall(r'^\d*\d+$', price)
    print(price)
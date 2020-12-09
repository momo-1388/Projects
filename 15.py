import requests
from bs4 import BeautifulSoup

r = requests.get("https://www.laptopsdirect.co.uk/ct/laptops-and-netbooks/laptops")

soup = BeautifulSoup(r.text, 'html.parser')

rams = soup.findAll('span', attrs={'class': 'proddescvalue'})
rams_string = []
for name in rams:
    rams_string.append(name.string)
   # print(name.string)

for ram in rams_string:
    print(ram)

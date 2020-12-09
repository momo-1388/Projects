import requests
from bs4 import BeautifulSoup
import re
in1 = input('Please Enter your model car : ')
in2 = input('Please Enter your tip car : ')
r = requests.get('https://bama.ir/car/all-brands/all-models/all-trims?price=30-40')
# print(r)
o = r.text
soup = BeautifulSoup(o, 'html.parser')
all_cars = soup.find_all('h2' , attrs={'itemprop':'name'})
for car in all_cars :
    d = re.sub(r'\s+' , ' ' , car.text).strip()
    b = d.split('،')
    e = list()
    for i in b :
        e.append(i.strip())
    if e[0] == in1:
        print(d)
#p = o['high']
#if p <= 20000.000 :
 #   print('Ohh You Win')

import requests
import bs4
import mysql.connector
from sklearn import tree

sql = mysql.connector.connect(
    user='root',
    host='localhost',
    password='13888',
    database='web'
)
table = 'pro'
cu = sql.cursor()

prc = list()
nac = list()

r = requests.get('https://www.truecar.com/used-cars-for-sale/listings/?sort%5B%5D=best_match')

soup = bs4.BeautifulSoup(r.text, 'html.parser')

names = soup.find_all('span', attrs={'class': "vehicle-header-make-model text-truncate"})
w_cars = soup.find_all('div', attrs={'data-test': "vehicleMileage"})
k_cars = soup.find_all('div', attrs={'data-qa': "ConditionHistory"})
maps = soup.find_all('div', attrs={'data-qa': "Location"})
prices = soup.find_all('h4', attrs={'data-test': "vehicleCardPricingBlockPrice"})
cars = list(zip(names, w_cars, k_cars, maps, prices))
for name, kar1, kar2, map_, price in cars:
    # cur = sql.cursor()
    # cur.execute('INSERT INTO {} VALUES (%s, %s, %s, %s, %s)'.format(table),
    #            (name.text, kar1.text, kar2.text, map_.text, price.text))
    print('_________________________')
    print('name : %s' % name.text)
    print('kar : %s' % kar1.text)
    print('karl : %s' % kar2.text)
    print('map : %s' % map_.text)
    print('price : %s' % price.text)

cu.execute('SELECT * FROM {}'.format(table))
my_res = cu.fetchall()

for res in my_res:
    nac.append(res[:4])
    prc.append(res[4])

clf = tree.DecisionTreeClassifier()
clf = clf.fit(nac, prc)

answer = clf.predict(input('Name : '), input('Kar1 : '), input('Kar2 : '), input('Map : '))
print(answer)
sql.commit()

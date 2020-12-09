import requests
from bs4 import BeautifulSoup
from sklearn import tree
import mysql.connector

clf = tree.DecisionTreeClassifier()

SQL = mysql.connector.connect(
    user='root',
    password='13888',
    host='localhost',
    database='web',
)
brand = input('Please Enter your brand :')
# شما حتما باید برند وشرکت ماشین را وارد کنید
brand.lower()
link_add = 'https://www.truecar.com/used-cars-for-sale/listings/%s' % brand

r = requests.get(link_add)

print(r)
response = r.text

oup = BeautifulSoup(response,'html.parser')
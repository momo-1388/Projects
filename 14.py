import requests
from bs4 import BeautifulSoup
import re
import mysql.connector

car_data = mysql.connector.connect(
    host="localhost",
    user="root",
    password=input("Please Enter Your MySQL password : "),
    database="web"
)

mycursor = car_data.cursor()
sql = "INSERT INTO all_cars (price, kar) VALUES (%s, %s)"
brand = input('Please Enter your brand :')
# شما حتما باید برند وشرکت ماشین را وارد کنید
brand.lower()
link_adderess = 'https://www.truecar.com/used-cars-for-sale/listings/%s' % brand
res = requests.get(link_adderess)
print(res)
response = res.text

soup = BeautifulSoup(response,'html.parser')

all_price = soup.find_all('h4' , attrs={'data-test' : 'vehicleCardPricingBlockPrice'})
all_carc = soup.find_all('div' , attrs={'data-qa' : 'MileageAndDiscount'})
all_cars = zip(all_price , all_carc)
n = 0
cars = []
# print(type(cars))
for car in all_cars :
    if n == 20 :
        break
    n+= 1
    # print(car[0].text , car[1].text)
    cars.append((car[0].text , car[1].text))
    cars.sort()
for i in cars :
    print(i[0] , i[1])

for i in cars:
    joj = i[1].split(' ')
    joj = joj[:2]
    joj =  ' '.join(joj)
    jog = i[0]
    mycursor = car_data.cursor()
    mycursor.execute('INSERT INTO all_car(price , kar) VALUES (%s , %s)', (jog, joj))


car_data.commit()
car_data.close()

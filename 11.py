import mysql.connector
from re import findall
def chek_email (email):
    while True :
        if findall(r'\w+@\w+\.\w+' ,email) == []:
            email = input("Email \ : expression@string.string \nPlease Enter you email : ")
        
        else :
            break
    return email
SQL = mysql.connector.connect(
    host="localhost",
    user="root",
    password=input("Please Enter Your MySQL password : "),
    database="jon"
)
mycursor = SQL.cursor()

email = input("Please Enter your email : ")
email = chek_email(email)
passw = input("Please Entyer your password : ")
mycursor.execute("INSERT INTO lop VALUES (%s , %s)" , (email , passw))

SQL.commit()
import mysql.connector


SQL = mysql.connector.connect(
    host="localhost",
    user="root",
    password=input("Please Enter Your MySQL password : "),
    database="persons"
)
my_cursor = SQL.cursor()

my_cursor.execute("SELECT * FROM person")

my_result = my_cursor.fetchall()

my_result.sort(key=lambda x: x[2])

n = len(my_result)

while n != 0:
    print(my_result[n - 1][0], my_result[n - 1][2], my_result[n - 1][1])
    n -= 1

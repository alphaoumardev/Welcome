import mysql.connector

my_database = mysql.connector.connect(
    host="localhost",
    user="root",
    password="bonjouroumar200"
)
print(my_database)

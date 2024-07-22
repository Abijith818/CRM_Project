import mysql.connector

dataBase = mysql.connector.connect(
    
    host = 'localhost',
    user = 'root',
    passwd = '@Bijith007'
)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE crmDB")

print("ALL DONE YEAAAH")
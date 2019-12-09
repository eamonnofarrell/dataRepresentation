import mysql.connector.authentication
mydb = mysql.connector.connect(   host="localhost",   user="root",   password="12345" )
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE datarepresentation")
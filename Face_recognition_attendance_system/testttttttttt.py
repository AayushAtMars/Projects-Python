import tkinter as tk
from tkinter import messagebox
import mysql.connector


# Function to validate login
con = mysql.connector.connect(host="localhost", username="root", password="aayu14",database="security")
my_cursor = con.cursor()

query= "select * from register"
my_cursor.execute(query)
a=my_cursor.fetchall()
print(a[0][6])

# a=my_cursor.execute("select email from register")
# b=my_cursor.execute("select password from register")

print(a)

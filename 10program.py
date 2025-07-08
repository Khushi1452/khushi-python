import sqlite3
connection=sqlite3.connect("example.db")
cur=connection.cursor()

while True:
    print("MENU: ")
    print("1.Create a Table")
    print("2.Delete a Table")
    print("3.Exit")
    choice=input("Enter a choice: ")

    if choice=='1':
        
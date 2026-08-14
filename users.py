import sqlite3


def get_users():
    with sqlite3.connect(r"C:\Users\Tami\Desktop\Pythons\pythonProject\Cooofffeee\coffee_db") as connect:
        cursor = connect.cursor()
        stmt = "SELECT Id, FirstName, Email FROM Users"
        users = cursor.execute(stmt).fetchall()
    return users

import sqlite3

connection = sqlite3.connect('Products.db')
cursor = connection.cursor()

def initiate_db():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INTEGER NOT NULL
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER NOT NULL,
    balance NOT NULL)
    ''')
def check_user(username):
    check_user = cursor.execute('SELECT username FROM Users WHERE username = ?', (f'{username}',))
    return check_user.fetchone()


def add_user(username, email,age):
    cursor.execute('INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)',
                    (f'{username}', f'{email}', f'{age}', '1000'))
    connection.commit()

def get_all_products():
    cursor.execute('SELECT title, description, price FROM Products')
    all_products = cursor.fetchall()
    return all_products

products = get_all_products()

print(check_user('Aleks'))
connection.commit()



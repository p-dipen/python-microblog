import sqlite3

connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute('Insert into user (username, password) values (?,?)', ('dipen','password'))

cur.execute('Insert into user (username, password) values (?,?)', ('dipen2','password2'))


connection.commit()

connection.close()

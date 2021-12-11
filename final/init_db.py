import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO List (title, user_id) VALUES (?,?)",
            ('Today List', '1')
            )

cur.execute("INSERT INTO Task (name, detail, list_id) VALUES (?, ?, ?)",
            ('First task', 'Survive final', '1')
            )

connection.commit()
connection.close()
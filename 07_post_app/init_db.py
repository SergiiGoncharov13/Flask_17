import sqlite3

connection = sqlite3.connect('blog.db')

with open('schema.sql') as f:
    connection.execute(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO posts (title, content) VALUES(?, ?)",
('Fisrt post', 'Contet to first post')
)

cur.execute("INSERT INTO posts (title, content) VALUES(?, ?)",
('Second post', 'Contet to second post')
)

connection.commit()
connection.close()
import sqlite3


connect = sqlite3.connect('app_sql.db')
connect.execute('''
    CREATE TABLE IF NOT EXISTS users (
    name TEXT,
    email TEXT,
    address TEXT
    )
''')


connect.commit()

connect.close()



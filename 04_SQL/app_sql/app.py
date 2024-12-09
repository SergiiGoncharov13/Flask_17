import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')


connect = sqlite3.connect('app_sql.db')
connect.execute('''
    CREATE TABLE IF NOT EXISTS users (
    name TEXT,
    email TEXT,
    address TEXT 
    )
''')

@app.route('/join', methods=['GET', 'POST'])
def join():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        address = request.form['address']
    
        with sqlite3.connect('app_sql.db') as users:
            cursor = users.cursor()
            cursor.execute('''
                INSERT INTO users
                (name, email, address)
                VALUES
                (?, ?, ?)
            ''',
            (name, email, address)
            )
            users.commit()
        return render_template('participants.html')
    else:
        return render_template('join.html')



@app.route('/participants')
def participants():
    connect = sqlite3.connect('app_sql.db')
    cursor = connect.cursor()
    cursor.execute('SELECT * FROM users')

    data = cursor.fetchall()
    return render_template("participants.html", data=data)



if __name__ == '__main__':
    app.run(debug=False)
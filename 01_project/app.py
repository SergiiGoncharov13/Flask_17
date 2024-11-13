from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/day')
def day():
    return f'Have a nice day'


@app.route('/hello')
def hello():
    return f'Hello'


if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template

app = Flask(__name__, template_folder='templates', static_folder='static')

works = [
    {'working': 'Telegram bot', 'year': 2024},
    {'working': 'Game', 'year': 2024},
    {'working': 'Web app', 'year': 2023},
]

@app.route('/')
def index():
    return render_template('base.html', title='Portfolio')


@app.route('/result')
def result():
    context = {
        'title': 'Result',
        'works': works
    }
    return render_template('results.html', **context)



if __name__ == '__main__':
    app.run(debug=True, port=8080)

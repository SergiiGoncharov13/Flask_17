from flask import Flask, render_template

app = Flask(__name__)


max_score = 100
test_name = 'Python Challenge'
students = [
    {'name':'Vlad', 'score': 100},
    {'name':'Svitoslav', 'score': 99},
    {'name':'Ustin', 'score': 100},
    {'name':'Victor', 'score': 79},
    {'name':'Yaroslav', 'score': 73},
]

@app.route('/')
def index():
    return render_template('base.html', title='It is worked')


@app.route('/result')
def result():
    context = {
        'title': 'Results',
        'students': students,
        'test_name': test_name,
        'max_score': max_score
    }
    return render_template('results.html', **context)



if __name__ == '__main__':
    app.run(debug=True)
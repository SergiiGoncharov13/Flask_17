from flask import Flask, render_template, request
import os

app = Flask(__name__)

filename = 'data.txt'

poll_data = {
    'question': 'Which framework do you use?',
    'fields': ['Flask', 'Django', 'FastAPI']
}


@app.route('/')
def root():
    return render_template('poll.html', data=poll_data)


@app.route('/poll')
def poll():
    vote = request.args.get("field")
    with open(filename, 'a') as f:
        f.write(vote + '\n')
    return render_template('result.html', data=poll_data, vote=vote)



if __name__ == '__main__':
    app.run(debug=True)
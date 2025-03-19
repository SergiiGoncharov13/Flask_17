import os
import uuid
import datetime 

from flask import Flask, render_template, request



app = Flask(__name__)

FILES_PATH = 'static/users_files'



@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')

    user_file = request.files.get('user_file')
    file_desc = request.files.get('file_desc')

    unique_filename = f'{str(uuid.uuid4().int)[:4]}_{user_file.filename}'

    file_path = os.path.join(FILES_PATH, unique_filename)
    if not user_file:
        return 'Chose your file to download'
    user_file.save(file_path)

    timestamp = datetime.datetime.now().strftime('%H:%M:%S')
    return render_template('index.html', message=f'File download succsses at time:{timestamp}')




if __name__ == '__main__':
    app.run(debug=True)
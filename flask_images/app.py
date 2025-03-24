import os
import uuid
import datetime 
from flask import Flask, render_template, request
from init_db import Session, UserFiles


app = Flask(__name__)

FILES_PATH = 'static/users_files'


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')

    user_file = request.files.get('user_file')
    file_desc = request.form.get('file_desc')

    unique_filename = f'{str(uuid.uuid4().int)[:4]}_{user_file.filename}'

    file_path = os.path.join(FILES_PATH, unique_filename)
    if not user_file:
        return 'Chose your file to download'
    user_file.save(file_path)

    with Session() as session:
        new_db_object = UserFiles(filename=unique_filename, file_description=file_desc)
        session.add(new_db_object)
        session.commit()

    timestamp = datetime.datetime.now().strftime('%H:%M:%S')
    return render_template('index.html', message=f'File download succsses at time:{timestamp}')
    
    
@app.route('/all_images')
def all_images():
    with Session() as session:
        all_data = session.query(UserFiles).all()
    return render_template('all_images.html', data=all_data)



if __name__ == '__main__':
    app.run(debug=True)
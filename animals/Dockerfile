# python version
FROM python:3.12-slim


# set working dir
WORKDIR /app

# copy requirements
COPY requirements.txt /app/
RUN pip install -r requirements.txt


# copy app code
COPY . /app

# port
EXPOSE 5000

# env for flask
ENV FLASK_APP=app.py
ENV FLASK_ENV=development

# command to run
CMD [ "flask", "run", "--host=0.0.0.0" ]
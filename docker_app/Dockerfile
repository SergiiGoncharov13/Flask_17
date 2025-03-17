# choose python
FROM python:3.10-slim

# choose workdir
WORKDIR /docker_app

# copy all files to image
COPY . /docker_app

# install requerements
RUN pip install -r requirements.txt


# choose port
EXPOSE 5000
EXPOSE 80

# command for running app
CMD [ "flask", "run", "--host=0.0.0.0" ]
# set base image (host OS)
FROM python:3.9

# set the working directory in the container
WORKDIR /code

# set environment variables used by Flask
# ENV SECRET_KEY=rlzaG7gIut6aNqG3Y@M0i5&7dslftQwi
# ENV FLASK_APP=main.py
# ENV FLASK_ENV=debug
# ENV SERVER_NAME=0.0.0.0:5000

# copy the dependencies file to the working directory
COPY ./requirements.txt .

# install external Python packages
RUN pip install -r requirements.txt

# copy the content of the local src directory to the working directory
COPY ./src .

# command to run on container start
CMD [ "python", "./main.py" ]
# pull official base image
FROM python:3.11.4-slim-buster

# set work directory
WORKDIR /code

# set env variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# instal deps
COPY ./requirements.txt /code/
RUN pip install -r requirements.txt

# copy project
COPY . .
# pull official base image
FROM python:3.11.4

# set env variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN pip install -U pip

# set work directory
WORKDIR /code/backend

# install deps
COPY ./requirements.txt /code/backend/
RUN pip install -r requirements.txt -U --no-cache

# copy project
COPY . /code/backend/
CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]
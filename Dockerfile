# pull official base image
FROM python

# set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE sentimental.settings.production
ENV SECRET_KEY DwuJyCBYF5kL9JjLILg47TCZKLWQ6LsA

COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt
# -*- coding: utf-8 -*-

import os
# from pathlib import Path, PureWindowsPath


# for local start
from dotenv import load_dotenv

load_dotenv()

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Dev preferences
    FLASK_APP = os.environ.get('FLASK_APP')
    FLASK_ENV = os.environ.get('FLASK_ENV')
    FLASK_DEBUG = os.environ.get('FLASK_DEBUG')

    # App preferences
    LANGUAGES = ['en', 'ru']

    # For Heroku
    LOG_TO_STDOUT = os.environ.get('LOG_TO_STDOUT')

    # Redis
    # REDIS_ROUTE = os.environ.get('REDIS_ROUTE')
    # REDIS_PORT = os.environ.get('REDIS_ROUTE')
    # REDIS_URL = os.environ.get('REDIS_URL') or 'redis://'

    # Celery
    # CELERY_RESULT_BACKEND = os.environ.get('CELERY_RESULT_BACKEND')
    # CELERY_BROKER_URL = os.environ.get('CELERY_BROKER_URL')
    # CELERY_ACCEPT_CONTENT = os.environ.get('CELERY_ACCEPT_CONTENT')
    # CELERY_RESULT_SERIALIZER = os.environ.get('CELERY_RESULT_SERIALIZER')
    # CELERY_TASK_SERIALIZER = os.environ.get('CELERY_TASK_SERIALIZER')

    CONFIG_FILE_FOR_DETECTOR = f'{basedir}/app/utils/config/haarcascade_frontalface_default.xml'
    ALLOWED_EXTENSIONS_PHOTO = {'png', 'jpg', 'jpeg', 'gif'}
    ALLOWED_HOSTS = ['http://127.0.0.1:5001']




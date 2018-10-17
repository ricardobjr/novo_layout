import os

DEBUG = True

SQLALCHEMY_DATABASE_URI = 'mysql://root@localhost:3306/highway_test'
SQLALCHEMY_TRACK_MODIFICATIONS = True

SECRET_KEY = os.urandom(24)

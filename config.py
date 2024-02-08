import os
basedir = os.path.abspath(os.path.dirname(__file__))
print(basedir)
class Config(object):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir,'database.db')
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your-will-never-guess'
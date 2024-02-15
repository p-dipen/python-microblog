import os
basedir = os.path.abspath(os.path.dirname(__file__))
print(basedir)
class Config(object):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir,'database.db')
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your-will-never-guess'
    MAIL_SERVER = 'sandbox.smtp.mailtrap.io'
    MAIL_PORT = 2525
    MAIL_USERNAME = 'cd2a94dbf77203'
    MAIL_PASSWORD = '70894b3d6b570e'
    ADMINS = ['ceb3a917f1-0dcee4+1@inbox.mailtrap.io','dparihar@canadianbusinesscollege.com']
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
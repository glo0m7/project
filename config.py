import os

basedir = os.path.abspath(os.path.dirname(__file__))

class config():
    SECRET_KEY = os.getenv("SECRET_KEY") or "hard to guess"
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir,"so.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    FLASK_ADMIN= os.getenv('FLASK_ADMIN')

    @staticmethod
    def init_app(app):
        pass


    DEBUG = True

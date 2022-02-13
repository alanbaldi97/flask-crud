from datetime import timedelta
from pickle import FALSE
from decouple import config
class Config:

    UPLOAD_FOLDER = 'uploads'

    STATIC_FOLDER = 'static'
    # TEMPLATE_FOLDER = '../frontend/dist/spa'
    # STATIC_URL_PATH = '/'
    DEBUG = True

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:root@localhost:5432/test_flask'
    SQLALCHEMY_BINDS = {}
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    DEBUG = True
    SECRET_KEY = ''

    #JWT
    JWT_SECRET_KEY = b'B\x8f\xdc;\x00y\x004V\xbb\x1f\x92\x01M\x04E'
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(days=365)
    JWT_ERROR_MESSAGE_KEY = 'msg'


class ProductionConfig:
    UPLOAD_FOLDER = 'uploads'

    STATIC_FOLDER = 'static'

    DEBUG = False
    SQLALCHEMY_DATABASE_URI = config('DATABASE_URL', default='localhost')
    SQLALCHEMY_BINDS = {}
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SECRET_KEY = ''

    #JWT
    JWT_SECRET_KEY = b'B\x8f\xdc;\x00y\x004V\xbb\x1f\x92\x01M\x04E'
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(days=365)
    JWT_ERROR_MESSAGE_KEY = 'msg'
    

config = {
    'development': Config,
    'production': ProductionConfig
}
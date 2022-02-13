from datetime import timedelta

class Config:

    UPLOAD_FOLDER = 'static/uploads'

    STATIC_FOLDER = 'static'

    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@localhost:3306/test_flask'
    SQLALCHEMY_BINDS = {}
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    DEBUG = True
    SECRET_KEY = ''

    #JWT
    JWT_SECRET_KEY = b'B\x8f\xdc;\x00y\x004V\xbb\x1f\x92\x01M\x04E'
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(minutes=5)
    JWT_ERROR_MESSAGE_KEY = 'msg'
import os


class Development(object):
    # Development environment configuration
    DEBUG = True
    TESTING = False
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')


class Production(object):
    # production environment configurations
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')




#FLASK_ENV = 'development'
#DATABASE_URL = 'sqlite://web/Sqlite-Data/blog_api_db.db'
JWT_SECRET_KEY = 'hi'

# user = os.environ['POSTGRES_USER']
# password = os.environ['POSTGRES_PASSWORD']
# host = os.environ['POSTGRES_HOST']
# database = os.environ['POSTGRES_DB']
# port = os.environ['POSTGRES_PORT']

DATABASE_CONNECTION_URI = 'sqlite:////web/Sqlite-Data/blog_api_db.db'

# 'sqlite+psycopg2:////web/Sqlite-Data/blog_api_db.db'

class Testing(object):

    TESTING = True
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_TEST_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS=False

app_config = {
    'development': Development,
    'production': Production,
    'testing': Testing
}

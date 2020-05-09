class Configuration(object):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URL = 'postgresql+psycopg2://postgres:geekbrains@localhost/blogonflask'
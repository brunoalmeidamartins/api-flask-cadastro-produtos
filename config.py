DEBUG = True

USERNAME = 'administrador'
PASSWORD = 'senhasecreta'
SERVER = 'localhost'
DB = 'flask_api'

SQLALCHEMY_DATABASE_URI = f'mysql://{USERNAME}:{PASSWORD}@{SERVER}/{DB}'
SQLALCHEMY_TRACK_MODIFICATIONS = True
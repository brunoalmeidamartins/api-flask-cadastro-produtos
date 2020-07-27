DEBUG = True

USERNAME = 'root'
PASSWORD = 'senhasecreta'
SERVER = 'mysqlsrv'
DB = 'flask_api'
PORT = 3306

SQLALCHEMY_DATABASE_URI = f'mysql://{USERNAME}:{PASSWORD}@{SERVER}:{PORT}/{DB}'
SQLALCHEMY_TRACK_MODIFICATIONS = True

SECRET_KEY = 'flask-api-cadastro-produto'
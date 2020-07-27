DEBUG = True

USERNAME = 'root'
PASSWORD = 'senhasecreta'
SERVER = 'mysqlsrv'
DB = 'flask_api'
PORT_DB = 3306

SQLALCHEMY_DATABASE_URI = f'mysql://{USERNAME}:{PASSWORD}@{SERVER}:{PORT_DB}/{DB}'
SQLALCHEMY_TRACK_MODIFICATIONS = True

SECRET_KEY = 'flask-api-cadastro-produto'
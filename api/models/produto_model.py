from api import db

class Produto(db.Model):
    __tablename__ = "produto"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    nome = db.Column(db.String(100), nullable= False)
    descricao = db.Column(db.String(250), nullable=False)
    data_validade = db.Column(db.Date, nullable=False)
    valor = db.Column(db.Float(precision=2), nullable=False)
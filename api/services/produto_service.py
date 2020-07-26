from ..models import produto_model
from api import db

def cadastrar_produto(produto):
    produto_db = produto_model.Produto(nome=produto.nome, descricao=produto.descricao,
                                        data_validade=produto.data_validade, valor=produto.valor)
    db.session.add(produto_db)
    db.session.commit()
    return produto_db

def listar_produtos():
    produtos = produto_model.Produto.query.all()
    return produtos

def listar_produto_id(id):
    produto = produto_model.Produto.query.filter_by(id=id).first()
    return produto

def editar_produto(produto_bd, produto_novo):
    produto_bd.nome = produto_novo.nome
    produto_bd.descricao = produto_novo.descricao
    produto_bd.data_validade = produto_novo.data_validade
    db.session.commit()

def remover_produto(produto):
    db.session.delete(produto)
    db.session.commit()


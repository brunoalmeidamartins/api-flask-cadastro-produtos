from flask_restful import Resource
from api import api
from ..schemas import produto_schema
from flask import request, make_response, jsonify
from ..entidades import produto
from ..services import produto_service
from ..pagination import paginate
from ..models.produto_model import Produto
from flask_jwt_extended import jwt_required

class ProdutoList(Resource):
    @jwt_required
    def get(self):
        #produtos = produto_service.listar_produtos()
        ps = produto_schema.ProdutoSchema(many=True)
        #return make_response(ps.jsonify(produtos), 200)
        return paginate(Produto, ps)
    
    def post(self):
        ps = produto_schema.ProdutoSchema()
        validate = ps.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            nome = request.json["nome"]
            descricao = request.json["descricao"]
            data_validade = request.json["data_validade"]
            produto_novo = produto.Produto(nome=nome, descricao=descricao, data_validade=data_validade)
            result = produto_service.cadastrar_produto(produto_novo)
            return make_response(ps.jsonify(result), 201)
class ProdutoDetail(Resource):
    def get(self, id):
        produto = produto_service.listar_produto_id(id)
        if produto is None:
            return make_response(jsonify("Produto não encontrado"), 400)
        ps = produto_schema.ProdutoSchema()
        return make_response(ps.jsonify(produto), 200)

    def put(self, id):
        produto_db = produto_service.listar_produto_id(id)
        if produto_db is None:
            return make_response(jsonify("Produto não encontrado"), 400)
        ps = produto_schema.ProdutoSchema()
        validate = ps.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            nome = request.json["nome"]
            descricao = request.json["descricao"]
            data_validade = request.json["data_validade"]
            produto_novo = produto.Produto(nome=nome, descricao=descricao,
                                            data_validade=data_validade)
            produto_service.editar_produto(produto_db, produto_novo)
            produto_atualizado = produto_service.listar_produto_id(id)
            return make_response(ps.jsonify(produto_atualizado), 200)

    def delete(self, id):
        produto = produto_service.listar_produto_id(id)
        if produto is None:
            return make_response(jsonify("Produto não encontrado"), 400)
        produto_service.remover_produto(produto)
        return make_response(' ', 204)

api.add_resource(ProdutoList, '/produtos')
api.add_resource(ProdutoDetail, '/produtos/<int:id>')
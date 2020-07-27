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
        """
        Listagem de todos os produtos
        ---
        parameters:
         - in: header
           name: Authorization
           type: string
           required: true
        responses:
          200:
            description: Lista de todos os produtos
            schema:
              id: Produto
              properties:
                produto_id:
                  type: integer
                nome:
                  type: string
                descricao:
                  type: string
                data_validade:
                  type: string
                valor:
                  type: float
        """
        #produtos = produto_service.listar_produtos()
        ps = produto_schema.ProdutoSchema(many=True)
        #return make_response(ps.jsonify(produtos), 200)
        return paginate(Produto, ps)

    @jwt_required
    def post(self):
        """
        Esta rota é responsável por cadastrar um novo produto
        ---
        parameters:
         - in: header
           name: Authorization
           type: string
           required: true
         - in: body
           name: Produto
           description: Criar novo produto
           schema:
             type: object
             required:
               - nome
               - descricao
               - data_validade
               - valor
             properties:
               nome:
                 type: string
               descricao:
                 type: string
               data_validade:
                 type: string
               valor:
                 type: float
        responses:
          201:
            description: Produto criado com sucesso
            schema:
              id: Produto
              properties:
                nome:
                  type: string
                descricao:
                  type: string
                data_validade:
                  type: string
                valor:
                  type: float
          400:
            description: Ocorreu um erro de validação
        """
        ps = produto_schema.ProdutoSchema()
        validate = ps.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            nome = request.json["nome"]
            descricao = request.json["descricao"]
            data_validade = request.json["data_validade"]
            valor = request.json["valor"]
            produto_novo = produto.Produto(nome=nome, descricao=descricao, data_validade=data_validade, valor=valor)
            result = produto_service.cadastrar_produto(produto_novo)
            return make_response(ps.jsonify(result), 201)
class ProdutoDetail(Resource):
    @jwt_required
    def get(self, id):
        """
        Retorna o produto que possui o ID como parâmetro
        ---
        parameters:
         - in: header
           name: Authorization
           type: string
           required: true
         - in: path
           name: id
           type: integer
           required: true
        responses:
          200:
            description: Produto que possui o ID enviado
            schema:
              id: Produto
              properties:
                produto_id:
                  type: integer
                nome:
                  type: string
                descricao:
                  type: string
                data_validade:
                  type: string
                valor:
                  type: float
          404:
            description: Produto não encontrado
        """
        produto = produto_service.listar_produto_id(id)
        if produto is None:
            return make_response(jsonify("Produto não encontrado"), 404)
        ps = produto_schema.ProdutoSchema()
        return make_response(ps.jsonify(produto), 200)

    @jwt_required
    def put(self, id):
        """
        Edita o produto que possui o ID passado com parâmetro
        ---
        parameters:
         - in: header
           name: Authorization
           type: string
           required: true
         - in: path
           name: id
           type: integer
           required: true
         - in: body
           name: Produto
           description: Editar produto
           schema:
             type: object
             required:
               - nome
               - descricao
               - data_validade
               - valor
             properties:
               nome:
                 type: string
               descricao:
                 type: string
               data_validade:
                 type: string
               valor:
                 type: float
        responses:
          200:
            description: Produto editado com sucesso
            schema:
              id: Produto
              properties:
                nome:
                  type: string
                descricao:
                  type: string
                data_validade:
                  type: string
                valor:
                  type: float
          400:
            description: Ocorreu um erro de validação
          404:
            description: Produto não encontrado
        """
        produto_db = produto_service.listar_produto_id(id)
        if produto_db is None:
            return make_response(jsonify("Produto não encontrado"), 404)
        ps = produto_schema.ProdutoSchema()
        validate = ps.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            nome = request.json["nome"]
            descricao = request.json["descricao"]
            data_validade = request.json["data_validade"]
            valor = request.json["valor"]
            produto_novo = produto.Produto(nome=nome, descricao=descricao,
                                            data_validade=data_validade, valor=valor)
            produto_service.editar_produto(produto_db, produto_novo)
            produto_atualizado = produto_service.listar_produto_id(id)
            return make_response(ps.jsonify(produto_atualizado), 200)

    @jwt_required
    def delete(self, id):
        """
        Remove o produto que possui o ID passado com parâmetro
        ---
        parameters:
         - in: header
           name: Authorization
           type: string
           required: true
         - in: path
           name: id
           type: integer
           required: true
        responses:
          204:
            description: Produto removido com sucesso
          404:
            description: Produto não encontrado
        """
        produto = produto_service.listar_produto_id(id)
        if produto is None:
            return make_response(jsonify("Produto não encontrado"), 404)
        produto_service.remover_produto(produto)
        return make_response(' ', 204)

api.add_resource(ProdutoList, '/produtos')
api.add_resource(ProdutoDetail, '/produtos/<int:id>')
from api import ma
from ..models import produto_model
from marshmallow import fields


class ProdutoSchema(ma.SQLAlchemySchema):
    class Meta:
        model = produto_model.Produto
        fields = ("id", "nome", "descricao", "data_validade", "valor", "_links")
    
    nome = fields.String(required=True)
    descricao = fields.String(required=True)
    data_validade = fields.Date(required=True)
    valor = fields.Float(required=True)
    _links = ma.Hyperlinks({
        "get": ma.URLFor("produtodetail", id="<id>"),
        "put": ma.URLFor("produtodetail", id="<id>"),
        "delete": ma.URLFor("produtodetail", id="<id>")
    })
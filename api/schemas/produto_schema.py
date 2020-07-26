from api import ma
from ..models import produto_model
from marshmallow import fields

#print(dir(ma))
class ProdutoSchema(ma.SQLAlchemySchema):
    class Meta:
        model = produto_model.Produto
        fields = ("id", "nome", "descricao", "data_validade")
    
    nome = fields.String(required=True)
    descricao = fields.String(required=True)
    data_validade = fields.Date(required=True)
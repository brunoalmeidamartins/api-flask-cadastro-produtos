class Produto():
    def __init__(self, nome, descricao, data_validade, valor):
        self.__nome = nome
        self.__descricao = descricao
        self.__data_validade = data_validade
        self.__valor = valor

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def descricao(self):
        return self.__descricao
    
    @descricao.setter
    def descricao(self, descricao):
        self.__descricao = descricao

    @property
    def data_validade(self):
        return self.__data_validade
    
    @data_validade.setter
    def data_validade(self, data_validade):
        self.__data_validade = data_validade

    @property
    def valor(self):
        return self.__valor
    
    @valor.setter
    def valor(self, valor):
        self.__valor = valor
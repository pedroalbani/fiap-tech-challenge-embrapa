class Manufatura:
    def __init__(self,nome,categoria,ano,quantidade,operacao):
        self.nome = nome
        self.categoria = categoria
        self.ano = ano
        self.quantidade = quantidade
        self.operacao = operacao

    def setNome(self,nome):
        self.nome = nome

    def setCategoria(self, categoria):
        self.categoria = categoria

    def setAno(self,ano):
        self.ano = ano

    def setQuantidade(self,quantidade):
        self.quantidade = quantidade

    def setOperacao(self,operacao):
        self.operacao = operacao
        
    def getNome(self):
        return self.nome

    def getCategoria(self):
        return self.categoria

    def getAno(self):
        return self.ano

    def getQuantidade(self):
        return self.quantidade

    def getOperacao(self):
        return self.operacao


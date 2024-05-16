class Comercio:
    def __init__(self,pais,ano,quantidade,valor,operacao):
        self.pais = pais
        self.ano = ano
        self.quantidade = quantidade
        self.valor = valor
        self.operacao = operacao
    
    def setPais(self,pais):
        self.pais = pais
    def setAno(self,ano):
        self.ano = ano
    def setQuantidade(self,quantidade):
        self.quantidade = quantidade
    def setValor(self,valor):
        self.valor = valor
    def setOperacao(self,operacao):
        self.operacao = operacao
        
    def getPais(self):
        return self.pais
    def getAno(self):
        return self.ano
    def getQuantidade(self):
        return self.quantidade
    def getValor(self):
        return self.valor
    def getOperacao(self):
        return self.operacao
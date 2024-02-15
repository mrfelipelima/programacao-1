class Semaforo:
    def __init__(self):
        self.corAtual = 'vermelho'

    def setPare(self):
        self.corAtual = 'vermelho'
        return self.corAtual
    
    def setAtencao(self):
        self.corAtual = 'amarelo'
        return self.corAtual
    
    def setSiga(self):
        self.corAtual = 'verde'
        return self.corAtual
    
    def getCorAtual(self):
        return self.corAtual
    
baraoComCesarPinheiro = Semaforo()

baraoComCesarPinheiro.setAtencao()

print(baraoComCesarPinheiro.getCorAtual())
        
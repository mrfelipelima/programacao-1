class Caldeira:
    def __init__(self):
        self.temperatura = 5
    
    def getTemperatura(self):
        return self.temperatura
    
    def setTemperatura(self, valor):
        self.temperatura = valor

forno = Caldeira()

print(forno.getTemperatura())
forno.setTemperatura(180)
print(forno.getTemperatura())
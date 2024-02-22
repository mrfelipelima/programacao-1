class Contador:
    def __init__(self):
        self.value = 0

    def zerar(self):
        self.value = 0

    def incrementar(self):
        self.value += 1
    
    def getValor(self):
        return self.value
    
contador = Contador()

print(contador.getValor())
contador.incrementar()
contador.incrementar()
print(contador.getValor())
contador.incrementar()
contador.incrementar()
print(contador.getValor())
contador.zerar()
print(contador.getValor())
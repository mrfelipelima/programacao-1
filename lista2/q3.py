class NumeroComplexo:
    def __init__(self, real, imaginario):
        self.real = real
        self.imaginario = imaginario

    def getReal(self):
        return self.real
    
    def getImaginario(self):
        return self.imaginario
    
    def setReal(self, real):
        self.real = real

    def setImaginario(self, imaginario):
        self.imaginario = imaginario

    def somar(self, novoReal, novoImaginario):
        self.real = self.real + novoReal
        self.imaginario = self.imaginario + novoImaginario
        return "parte real: {}, parte imaginária: {}".format(self.real, self.imaginario)
    
    def subtrair(self, novoReal, novoImaginario):
        self.real = self.real - novoReal
        self.imaginario = self.imaginario - novoImaginario
        return "parte real: {}, parte imaginária: {}".format(self.real, self.imaginario)
    
    def multiplicar(self, novoReal, novoImaginario):
        self.real = (self.real * novoReal) - (self.imaginario * novoImaginario)
        self.imaginario = (self.real * novoImaginario) + (self.imaginario * novoReal)
        return "parte real: {}, parte imaginária: {}".format(self.real, self.imaginario)
    
    def compare(self, novoReal, novoImaginario):
        return (self.real == novoReal) and (self.imaginario == novoImaginario)
    
    def toString(self):
        return "parte real: , {}, parte imaginária: , {}".format(self.real, self.imaginario)
    
    
calc = NumeroComplexo(3, 5)

print(calc.getReal())
print(calc.getImaginario())

calc.setReal(7)
calc.setImaginario(9)
print(calc.getReal())
print(calc.getImaginario())

print(calc.somar(4,2))
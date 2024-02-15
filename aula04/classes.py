class Calc:
    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2

    def soma(self):
        return self.n1 + self.n2
    
    def subtracao(self):
        return self.n1 - self.n2
    
    def multiplicacao(self):
        return self.n1 * self.n2
    
    def divisao(self):
        return self.n1 / self.n2
    
sum = Calc(3, 2).soma()

print(sum)

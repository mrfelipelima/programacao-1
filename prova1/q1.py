class contaCorrente:
    def __init__(self, nomeCor, numCon, saldoCon):
        self.nome = nomeCor
        self.num = numCon
        self.saldo = saldoCon
    
    def get_saldo(self):
        return self.saldo
    def set_saldo(self, saldoCon):
        self.saldo = saldoCon

    def get_nConta(self):
        return self.num
    def set_nConta(self, numCon):
        self.num = numCon

    def get_nome(self):
        return self.nome
    def set_nome(self, nomeCor):
        self.nome = nomeCor

    def Zerado(self):
        if(self.saldo == 0):
            return print("O saldo da sua conta está zerado.")
        else:
            return print("O seu saldo é igual a {} ".format(self.saldo))

    def compra(self, valor_compra):
        if(valor_compra > self.saldo):
            return print("Compra não aprovada")
        else:
            self.saldo = self.saldo - valor_compra
            return print("Compra aprovada")
        
felipe = contaCorrente('Felipe Lima', 989000, 100)

print(felipe.get_saldo())
felipe.Zerado()
felipe.compra(80)
print(felipe.get_saldo())

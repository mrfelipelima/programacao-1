class Continente:
    def __init__(self, continente):
        self.continente = continente

    paises = []

    def adicionarPais(self, pais, continente, dimensao, populacao):
        self.paises.append({
            'pais': pais,
            'continente': continente,
            'dimensao': dimensao,
            'populacao': populacao
        })
    
    def getDimensaoTotal(self):
        soma = 0
        for paises in self.paises:
            soma += paises.dimensao
        return soma


americaDoSul = Continente('América do Sul')

print(americaDoSul.continente)
americaDoSul.adicionarPais('BRA', 'América do Sul', 1000, 500)
americaDoSul.adicionarPais('ARG', 'América do Sul', 500, 100)
print(americaDoSul.paises[1]['dimensao'])

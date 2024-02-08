class Pizza:
    def __init__(self):
        self.massa = "tradicional"
        self.ncondimentos = 2

    def get_massa(self):
        return self.massa
    
    def set_massa(self, massa):
        self.massa = massa

    def set_ncondimentos(self, ncondimentos):
        self.ncondimentos = ncondimentos
    
    def get_ncondimentos(self):
        return self.ncondimentos
    

quatroQueijos = Pizza()

print("Massa da pizza: ", quatroQueijos.get_massa())

quatroQueijos.set_massa("Premium")

print("Massa da pizza: ", quatroQueijos.get_massa())

print("Número de condimentos", quatroQueijos.get_ncondimentos())

quatroQueijos.set_ncondimentos(6)

print("Número de condimentos", quatroQueijos.get_ncondimentos())
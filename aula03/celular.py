class Celular:
    def __init__(self):
        self.number = 00

    def set_number(self, number):
        self.number = number
    
    def get_number(self):
        return self.number

felipe = Celular()

print(felipe.get_number())

felipe.set_number(991608939)

print(felipe.get_number())
def area(frente, fundo):
    return frente * fundo

a = float(input("Digite o valor do fundo do terreno: "))
b = float(input("Digite o valor do frente do terreno: "))

print("A área do terreno é: ", area(a, b))
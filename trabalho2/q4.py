lista = []

for i in range(10):
    valor = int(input("Digite um número: "))
    if (valor % 2 == 0):
        lista.append(valor + 1)
    else:
        lista.append(valor)

print(lista)

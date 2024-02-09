nome = input("Coloque o nome do produto: ")
valor = float(input("Coloque o valor do produto: "))
quantidade = int(input("Coloque a quantidade do produto: "))

if (quantidade <= 10):
    print("O produto", nome, "não possui desconto. Total a pagar: R$", valor * quantidade)

if ((quantidade >= 11) and (quantidade <= 20)):
    desconto = valor * 0.10
    valorFinal = (valor * quantidade) - desconto
    print("O produto ", nome, "possui 10% de desconto, totalizando: R$ ", desconto, "Total a pagar: R$", valorFinal)

if ((quantidade >= 21) and (quantidade <= 50)):
    desconto = valor * 0.20
    valorFinal = (valor * quantidade) - desconto
    print("O produto ", nome, "possui 20% de desconto, totalizando: R$ ", desconto, "Total a pagar: R$", valorFinal)

if (quantidade > 50):
    desconto = valor * 0.25
    valorFinal = (valor * quantidade) - desconto
    print("O produto ", nome, "possui 25% de desconto, totalizando: R$ ", desconto, "Total a pagar: R$", valorFinal)
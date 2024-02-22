names = []
amount = []

for i in range(5):
    names.append(input("Insira o nome: "))
    amount.append(input("Insira o saldo: "))

print("===== LISTA DE CLIENTES =====")
print("NOME", "SALDO", "CONTA")
for i in range(5):
    print(names[i-1], amount[i-1], "#", i)
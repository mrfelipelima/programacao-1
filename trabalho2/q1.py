names = []
amount = []

for i in range(5):
    names.append(input("Insira o nome: "))
    amount.append(input("Insira o saldo: "))

print("===== LISTA DE CLIENTES =====")
print("NOME", "\tSALDO", "\tCONTA")
for i in range(5):
    print("{}".format(names[i-1]), "\t{}".format(amount[i-1]), "\t# {}".format(i))
import os

codigos = []
pesos = []
alturas = []

counter = 0
data = input("(Digite 0 para sair)\nDigite o código do do cliente {}: ".format(counter + 1))

# Verifica se o usuário digitou 0 no primeiro código, caso sim, encerra o programa
# pois não haverá dados para serem calculados.
if data == "0":
    print("Nenhum código informado, encerrando programa.")
    quit()

# Loop de aquisição de dados
while data:
    # Verifica se o usuário digitou 0 no campo 'código' para encerrar o loop
    if (data == "0"):
        break
    
    # Se o usuário não digitou 0 no campo código, inclui o valor do código
    # ao final da lista de códigos
    codigos.append(int(data))

    # Solicita o peso do cliente
    data = input("Digite o peso do cliente {}: ".format(counter + 1))
    # Inclui o peso no final da lista de pesos
    pesos.append(float(data))
    data = input("Digite a altura do cliente {}: ".format(counter + 1))
    alturas.append(float(data))

    counter += 1
    
    data = input("(Digite 0 para sair)\nDigite o código do do cliente {}: ".format(counter + 1))

# A função os.system foi chamada para limpar o console antes de apresentar os resultados
os.system('cls' if os.name == 'NT' else 'clear')

print("===== RESULTADOS =====")
# Apresenta o cliente mais alto e o seu código
mais_alto = max(alturas)
indice_mais_alto = alturas.index(mais_alto)
print("O cliente com código", codigos[indice_mais_alto], "é o mais alto, possuindo", mais_alto, "de altura.")

# Apresenta o cliente mais baixo e o seu código
mais_baixo = min(alturas)
indice_mais_baixo = alturas.index(mais_baixo)
print("O cliente com código", codigos[indice_mais_baixo], "é o mais baixo, possuindo", mais_baixo, "de altura.")

# Apresenta o cliente mais gordo e o seu código
mais_pesado = max(pesos)
indice_mais_pesado = pesos.index(mais_pesado)
print("O cliente com código", codigos[indice_mais_pesado], "é o cliente mais gordo, possuindo", mais_pesado, "de peso.")

# Apresenta o cliente mais magro e o seu código
menos_pesado = min(pesos)
indice_menos_pesado = pesos.index(menos_pesado)
print("O cliente com código", codigos[indice_menos_pesado], "é o cliente mais magro, possuindo", menos_pesado, "de peso.")

# Apresenta a média de alturas
media_de_tamanhos = sum(alturas) / len(alturas)
print("A média de alturas é: ", media_de_tamanhos)

# Apresenta a média de pesos
media_de_pesos = sum(pesos) / len(pesos)
print("A média de pesos é: ", media_de_pesos)

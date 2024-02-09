# Solicita as coordenadas do primeiro ponto:
p1x = int(input("Entre com o valor de ponto 1 em x: "))
p1y = int(input("Entre com o valor de ponto 1 em y: "))
p1z = int(input("Entre com o valor de ponto 1 em z: "))

# Solicita as coordenadas do segundo ponto:
p2x = int(input("Entre com o valor de ponto 2 em x: "))
p2y = int(input("Entre com o valor de ponto 2 em y: "))
p2z = int(input("Entre com o valor de ponto 2 em z: "))

# Calcula a diferença entre os pontos
dif_x = p1x - p2x
dif_y = p1y - p2y
dif_z = p1z - p2z

# Calcula a soma do quadrado das diferenças
soma_quadrados = (dif_x ** 2) + (dif_y ** 2) + (dif_z ** 2)

# Calcula a raíz quadrada da soma dos quadrados
distancia = soma_quadrados ** 0.5

print("A distância entre dois pontos é: ", distancia)

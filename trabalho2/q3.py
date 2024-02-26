def criar_matriz():
    matriz = []
    for i in range(3):
        linha = []
        for j in range(3):
            elemento = input(f"Digite o elemento da posição ({i + 1}, {j + 1}): ")
            linha.append(elemento)
        matriz.append(linha)
    return matriz

# Função para imprimir a matriz transposta
def imprimir_transposta(matriz):
    print("Matriz Transposta:")
    for j in range(3):
        for i in range(3):
            print(matriz[i][j], end=" ")
        print()

# Criar matriz
matriz_original = criar_matriz()

# Imprimir matriz original
print("Matriz Original:")
for linha in matriz_original:
    print(linha)

# Calcular e imprimir a transposta
imprimir_transposta(matriz_original)

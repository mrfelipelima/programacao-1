a = float(input("Insira o primeiro número: "))
b = float(input("Insira o segundo número: "))

def paridade(a, b):
    ok = (a % 2) != (b % 2)
    return ok

print(paridade(a,b))
a = float(input("Entre com o valor da variável a: "))
b = float(input("Entre com o valor da variável b: "))
c = float(input("Entre com o valor da variável c: "))

delta = (b ** 2) - (4 * a * c)

x1 = (-b + delta**0.5) / (2 * a)
x2 = (-b - delta**0.5) / (2 * a)

print("Raiz positiva: ", x1)
print("Raiz positiva: ", x2)

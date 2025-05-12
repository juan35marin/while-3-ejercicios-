# Solicitar al usuario un número
n = int(input("Ingresa un número natural: "))

# Usando un ciclo for
suma_for = 0
for i in range(1, n + 1):
    suma_for += i
print(f"Suma usando for: {suma_for}")

# Usando un ciclo while
suma_while = 0
i = 1
while i <= n:
    suma_while += i
    i += 1
print(f"Suma usando while: {suma_while}")
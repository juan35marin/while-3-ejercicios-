def factorial_for(n):
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial

# Usando un bucle while
def factorial_while(n):
    factorial = 1
    i = 1
    while i <= n:
        factorial *= i
        i += 1
    return factorial

# Ejemplo de uso
numero = int(input("Introduce un número: "))

print("Factorial usando for:", factorial_for(numero))
print("Factorial usando while:", factorial_while(numero))
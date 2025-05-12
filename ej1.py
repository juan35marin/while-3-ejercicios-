# Imprimir los primeros 20 números pares usando un ciclo for
print("Primeros 20 números pares:")
for i in range(1, 21):  # El ciclo va del 1 al 20 (inclusive)
    print(i * 2)  # Multiplicamos por 2 para obtener números pares: 2, 4, 6, ..., 40

# Imprimir los primeros 15 números impares usando un ciclo while
print("\nPrimeros 15 números impares:")
contador = 0  # Contador para saber cuántos números impares se han impreso
numero = 1  # Empezamos con el primer número impar

while contador < 15:  # Se repite hasta imprimir 15 impares
    print(numero)  # Imprimimos el número impar actual
    numero += 2  # Sumamos 2 para obtener el siguiente número impar
    contador += 1  # Aumentamos el contador en 1
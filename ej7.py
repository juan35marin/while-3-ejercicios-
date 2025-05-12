# Contraseña correcta
contraseña_correcta = "riwi123"

# Contador de intentos
intentos = 0
max_intentos = 3

# Bucle de validación
while intentos < max_intentos:
    contraseña = input("Ingresa la contraseña: ")
    if contraseña == contraseña_correcta:
        print("¡Contraseña correcta! Bienvenido.")
        break
    else:
        intentos += 1
        print(f"Contraseña incorrecta. Intento {intentos} de {max_intentos}.")

# Si se exceden los intentos
if intentos == max_intentos:
    print("Has excedido el número máximo de intentos. Acceso denegado.")

saldo = 0  # Saldo inicial del usuario

# Iniciamos un bucle infinito para mostrar el menú hasta que el usuario decida salir
while True:
    # Mostrar el menú principal
    print("\n--- Cajero Automático ---")
    print("1. Ver saldo")
    print("2. Depositar dinero")
    print("3. Retirar dinero")
    print("4. Salir")
    
    # Pedir al usuario que elija una opción
    opcion = input("Elige una opción: ")

    # Opción 1: Ver el saldo actual
    if opcion == "1":
        print(f"Tu saldo actual es: ${saldo:.2f}")
    
    # Opción 2: Depositar dinero
    elif opcion == "2":
        deposito = float(input("¿Cuánto deseas depositar? $"))  # Pedir el monto a depositar
        if deposito > 0:
            saldo += deposito  # Sumar al saldo
            print(f"Has depositado ${deposito:.2f}. Nuevo saldo: ${saldo:.2f}")
        else:
            print("El monto debe ser mayor a cero.")  # Validación para evitar depósitos negativos o nulos
    
    # Opción 3: Retirar dinero
    elif opcion == "3":
        retiro = float(input("¿Cuánto deseas retirar? $"))  # Pedir el monto a retirar
        if retiro > saldo:
            print("Fondos insuficientes.")  # No permitir retirar más de lo que hay en saldo
        elif retiro <= 0:
            print("El monto debe ser mayor a cero.")  # Validar que el monto sea positivo
        else:
            saldo -= retiro  # Restar del saldo
            print(f"Has retirado ${retiro:.2f}. Nuevo saldo: ${saldo:.2f}")
    
    # Opción 4: Salir del programa
    elif opcion == "4":
        print("Gracias por usar el cajero. ¡Hasta luego!")
        break  # Romper el bucle while y salir del programa

    # En caso de que el usuario ingrese una opción inválida
    else:
        print("Opción inválida. Intenta de nuevo.")

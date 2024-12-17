# Escribe un programa que solicite al usuario un número entero positivo y
# luego calcule la cantidad de dígitos del número utilizando un bucle while.

numero = int(input("Introduce un numero entero positivo."))

if numero <= 0:
    print("introduce un numero entero positivo.")
else:
    cantidad_digitos = 0
    while numero > 0:
        numero = numero // 10 
        cantidad_digitos += 1

        print(f"el numero tiene {cantidad_digitos} digitos.")
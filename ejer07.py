# Escribe un programa que solicite al usuario un número entero positivo y
# luego imprima la suma de los primeros n números pares
# utilizando un bucle while.

n = int(input("Introduce un numero entero posoitivo:"))
suma_pares = 0
contador = 1
numero_par = 2

while contador <= n:
    suma_pares += numero_par
    numero_par += 2
    contador += 1

    print(f"la suma de los primero {n} numeros pares es: {suma_pares}")
# Escribe un programa que solicite al usuario un número entero positivo y
#  luego calcule la suma de todos los números divisibles por 3 desde 1 
#  hasta ese número utilizando un bucle while.

numero = int(input("Introduce un numero entero positivo "))

if numero <= 0:
    print("introduce un numero entero positivo mayor que cero.")
else:
    suma = 0 
    i = 1

while i <= numero:
    if i % 3 == 0:
        suma += i
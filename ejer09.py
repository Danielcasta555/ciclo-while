# Escribe un programa que solicite al usuario un número entero positivo y luego imprima todos los números entre 1 y 
# ese número en orden inverso utilizando un bucle while.

numero = int(input("Introduce un numero entero positivo."))
contador = numero

while contador >= 1:
    print(contador)
    contador -= 1
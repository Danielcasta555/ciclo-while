# Escribe un programa que solicite al usuario un número entero positivo y
#  luego imprima los primeros n números impares utilizando un bucle while.

n = int(input("Introduce un numero entero positivo:"))
contador = 0
numero_impar = 1

while contador <= n:
    print(numero_impar)
    numero_impar += 2
    contador += 1
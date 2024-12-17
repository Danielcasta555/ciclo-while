# Escribe un programa que solicite al usuario dos 
# números enteros positivos y luego imprima todos los números entre
#  ellos (inclusive) utilizando un bucle while.


num1 = int(input("Introduce el primer numero entero positivo "))
num2 = int(input("Introduce el segundo numero entero positivo"))

if num1 > num2:
    num1, num2 = num2, num1
contador = num1

while contador <= num2:
    print(contador)
    contador += 1

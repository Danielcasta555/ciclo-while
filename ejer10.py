# Escribe un programa que solicite al usuario dos números enteros positivos y 
# luego imprima la suma de todos los números entre ellos (inclusive) utilizando un bucle while.

num1 = int(input("Introduce el primer numero entero positivo:"))
num2 = int(input("Introduce el segundo numero entero positivo:"))

contador = num1
suma_total = 0

if num1 > num2:
    num1, num2 = num2, num1

while contador <= num2:
    suma_total += contador
    contador += 1

    print(f"la suma de todos los numeros entre {num1} y {num2} (inclusive) es: {suma_total}")
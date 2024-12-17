# Escribe un programa que solicite al usuario un número entero positivo y
# luego imprima el promedio de todos los números desde 1 hasta ese número utilizando un bucle while.

numero = int(input("Introduce un numero entero positivo:"))
suma_total = 0 
contador = 1

while contador <= numero:
    suma_total += contador
    contador += 1

promedio = suma_total / numero
print(f"el promedio de todos los numeros desde 1 hasta {numero} es: {promedio}")
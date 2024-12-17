# Escribe un programa que solicite al usuario un número entero positivo y
# luego imprima la suma de los números de Fibonacci hasta ese número utilizando un bucle while.

numero = int(input("Introduce un numero entero positivo:"))
a, b = 0, 1
suma_fibonacci = 0

while a <= numero:
    suma_fibonacci += a
    a, b = b, a + b
print(f"la suma de los numeros de fibonacci hasta {numero} es: {suma_fibonacci}")
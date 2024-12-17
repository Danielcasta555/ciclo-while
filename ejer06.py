# Escribe un programa que solicite al usuario un número entero positivo y luego imprima la suma de los cuadrados de todos los números desde 1 
# hasta ese número utilizando un bucle while.

numero = int(input("introduce un numero entero positivo:"))

if numero <= 0:
    print("introduce un numero entero positivo mayo que cero.")
else:
    suma = 0
    i = 1 

    while i <= numero:
        suma += i ** 2
        i + 1

        print(f"la suma de los numero desde 1 hasta {numero} es: {suma}")
# Escribe un programa que solicite al usuario dos números enteros positivos y 
# luego imprima la tabla de multiplicar del primer número hasta el segundo número utilizando un bucle while.

# Solicitar al usuario dos números enteros positivos
num1 = int(input("Introduce el primer número entero positivo: "))
num2 = int(input("Introduce el segundo número entero positivo: "))


if num1 > num2:
    num1, num2 = num2, num1


contador = num1


while contador <= num2:
    print(f"\nTabla de multiplicar del {contador}:")
    i = 1
    while i <= 10:
        print(f"{contador} x {i} = {contador * i}")
        i += 1
    contador += 1
 
     
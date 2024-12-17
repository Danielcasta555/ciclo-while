# Escribe un programa que solicite al usuario un número entero positivo y 
# luego imprima si el número es un número de Armstrong utilizando un bucle while.

numero = int(input("Introduce un numero entero positivo."))
numero_str = str(numero)
num_digitos = len(numero_str)

suma_digitos = 0
contador = 0

while contador < num_digitos:
    digito = int(numero_str[contador])
    suma_digitos += digito ** num_digitos
    contador += 1

    if suma_digitos == numero:
        print(f"{numero} es un numero de armstrong.")
    else:
        print(f"{numero} no es numero de armstrong")
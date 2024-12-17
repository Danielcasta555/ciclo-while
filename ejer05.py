# Escribe un programa que solicite al usuario un número entero positivo y 
# luego imprima todos los números primos menores o iguales a ese número utilizando un bucle while.


def es_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


numero = int(input("Introduce un número entero positivo: "))


contador = 2


while contador <= numero:
    if es_primo(contador):
        print(contador)
    contador += 1
  

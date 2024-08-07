#Ejercicio 1
def todos_positivos(lista):
    positivos = 0
    for numero in lista:
        if numero >=0:
            positivos += 1
    if positivos == len(lista):
        return True
    else:
        return False
lista_numeros = [1,2,1,4,5,6,7]
#Ejercicio 2
def suma_menores(lista):
    suma = 0
    for numero in lista:
        if numero > 0 and numero < 1000:
            suma = numero+suma
    return suma
lista_numeros = [1,3,-4,6,500,300]
#Ejercicio 3
def cantidad_pares(lista):
    pares = 0
    for numero in lista:
        if numero%2 == 0:
            pares += 1
    return pares
lista_numeros = [1,2,3,4,5,6,7]
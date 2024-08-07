import random
#Ejercicio 1
def lanzar_dados():
    dado_1 = random.randint(1,6)
    dado_2 = random.randint(1,6)
    return dado_1, dado_2
def evaluar_jugada (puntuacion_1, puntuacion_2):
    suma_dados = puntuacion_1+puntuacion_2
    if suma_dados <= 6:
        return f"La suma de tus dados es {suma_dados}. Lamentable"
    elif suma_dados > 6 and suma_dados < 10:
        return f"La suma de tus dados es {suma_dados}. Tienes buenas chances"
    elif suma_dados <= 10:
        return f"La suma de tus dados es {suma_dados}. Parece una jugada ganadora"
#Ejercicio 2
lista_numeros = [1,2,15,7,2]
def reducir_lista(lista):
    lista_reducida = []
    numero_max = 0
    for numero in lista:
        if numero not in lista_reducida:
            lista_reducida.append(numero)
    for numero in lista_reducida:
        if numero > numero_max:
            numero_max = numero
    lista_reducida.remove(numero_max)
    return lista_reducida
def promedio(lista):
    suma = 0
    for numero in lista:
        suma = suma + numero
    return suma/ len(lista)
#Ejercicio 3
lista_numeros = [1,12,23,79]
def lanzar_moneda():
    moneda = ["Cara","Cruz"]
    lanzamiento = random.randint(0,1)
    return moneda[lanzamiento]
def probar_suerte(resultado_lanzamiento, lista):
    if resultado_lanzamiento == "Cara":
        print("La lista se autodestruirá")
        lista = list()
        return lista
    else:
        print("La lista fue salvada")
        return lista
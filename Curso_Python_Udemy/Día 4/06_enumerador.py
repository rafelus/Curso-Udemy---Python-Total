#Ejercicio 1
lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]
for lista in enumerate(lista_nombres):
    nombre = lista[1]
    indice = lista[0]
    print(f'{nombre} se encuentra en el índice {indice}')
#Ejercicio 2
lista_indices = list(enumerate("Python"))
#Ejercicio 3
lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]
for elemento in enumerate(lista_nombres):
    if elemento[1].startswith("M"):
        print(elemento[0])
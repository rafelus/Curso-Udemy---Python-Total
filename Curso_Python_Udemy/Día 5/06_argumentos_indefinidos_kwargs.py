#Ejercicio 1
def cantidad_atributos(**kwargs):
    cantidad = 0
    for kwarg in kwargs:
        cantidad += 1
    return cantidad
#Ejercicio 2
def lista_atributos(**kwargs):
    lista = []
    for valor in kwargs.values():
        lista.append(valor)
    return lista
#Ejercicio 3
def describir_persona(nombre, **kwargs):
    print(f"Características de {nombre}:")
    for nombre_argumento,valor_argumento in kwargs.items():
        print(f"{nombre_argumento}: {valor_argumento}")
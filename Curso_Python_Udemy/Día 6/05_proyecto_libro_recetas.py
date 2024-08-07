"""
*************************************************************************************************
Aquí viene la consigna: tu código le va a dar primero la bienvenida al usuario, le va a informar
la ruta de acceso al directorio donde se encuentra nuestra carpeta de recetas, le va a informar
cuántas recetas hay en total dentro de esa carpeta, y luego le va a pedir que elija una de
estas opciones que tenemos aquí:
1. La opción 1 le va a preguntar qué categoría elige (carnes, ensaladas, etc.), y una vez que
el usuario elija una, le va a preguntar qué receta quiere leer, y mostrar su contenido.
2. En la opción 2 también se le va a hacer elegir una categoría, pero luego le va a pedir que
escriba el nombre y el contenido de la nueva receta que quiere crear, y el programa va
a crear ese archivo en el lugar correcto.
3. La opción 3 le va a preguntar el nombre de la categoría que quiere crear y va a generar
una carpeta nueva con ese nombre.
4. La opción 4, hará todo lo mismo que la opción uno, pero en vez de leer la receta, la va
a eliminar
5. La opción 5, le va a preguntar qué categoría quiere eliminar
6. Finalmente, la opción 6 simplemente va a finalizar la ejecución del código.
*************************************************************************************************
"""

import os
from os import system
from pathlib import Path


def creacion_carpetas_de_recetas():
    """
    Primero se consigue la ruta base desde la que se va a escribir el código.
    """
    ruta_base = os.getcwd()
    """
    Después se intenta acceder al directorio del Libro de Recetas y si no existe se crea el directorio 
    con todas las subcarpetas y archivos que contiene al inicio del ejercicio.
    (así se evita el fallo tanto si ya existe el directorio como si no existe)
    """
    try:
        os.chdir(f"{ruta_base}\\05_Libro de Recetas")

    except FileNotFoundError:
        os.mkdir("05_Libro de Recetas")
        os.chdir(f"{ruta_base}\\05_Libro de Recetas")
        os.mkdir("CARNES")
        os.mkdir("ENSALADAS")
        os.mkdir("PASTAS")
        os.mkdir("POSTRES")
        ruta_actual = os.getcwd()

        os.chdir(f"{ruta_actual}\\CARNES")
        receta_carne_1 = open("Entrecot al Malbec.txt", "w")
        receta_carne_1.write("Esta es la receta del Entrecot al Malbec")
        receta_carne_1.close()
        receta_carne_2 = open("Matambre a la Pizza.txt", "w")
        receta_carne_2.write("Esta es la receta del Matambre a la Pizza")
        receta_carne_2.close()

        os.chdir(f"{ruta_actual}\\ENSALADAS")
        receta_ensalada_1 = open("Ensalada Griega.txt", "w")
        receta_ensalada_1.write("Esta es la receta de la Ensalada Griega")
        receta_ensalada_1.close()
        receta_ensalada_2 = open("Ensalada Mediterranea.txt", "w")
        receta_ensalada_2.write("Esta es la receta de la Ensalada Mediterranea")
        receta_ensalada_2.close()

        os.chdir(f"{ruta_actual}\\PASTAS")
        receta_pasta_1 = open("Canelones de Espinaca.txt", "w")
        receta_pasta_1.write("Esta es la receta de los Canelones de Espinaca")
        receta_pasta_1.close()
        receta_pasta_2 = open("Ravioles de Ricotta.txt", "w")
        receta_pasta_2.write("Esta es la receta de los Ravioles de Ricotta")
        receta_pasta_2.close()

        os.chdir(f"{ruta_actual}\\POSTRES")
        receta_postre_1 = open("Compota de Manzana.txt", "w")
        receta_postre_1.write("Esta es la receta de la Compota de Manzana")
        receta_postre_1.close()
        receta_postre_2 = open("Tarta de Frambuesa.txt", "w")
        receta_postre_2.write("Esta es la receta de la Tarta de Frambuesa")
        receta_postre_2.close()

        os.chdir(f"{ruta_base}\\05_Libro de Recetas")

    ruta_base = os.getcwd()
    return ruta_base


def ruta_inicial(ruta_principal):
    os.chdir(ruta_principal)


def bienvenida():
    ruta_libro_recetas = os.getcwd()

    print("*" * 79)
    print("Bienvenido al Libro de Recetas!! El libro en el podrás consultar y escribir tus recetas favoritas.")
    print("-" * 79)
    print(f"Si deseas consultar de forma manual las recetas que tienes guardas lo prodrás\nhacer a partir de la"
          f" siguiente ruta: \n{ruta_libro_recetas}")
    """
    print("*" * 79)
    input("Presione 'ENTER' para continuar")
    system("cls")
    print("*" * 79)
    print("Actualmente, estas son todas las recetas que hay disponibles:")
    print("-" * 79)
    for txt in Path(ruta_libro_recetas).glob("**/*.txt"):
        print(txt.stem)
    """
    presiona_enter()


def menu_de_inicio():
    lista_opciones = ["1", "2", "3", "4", "5", "6"]
    opcion_elegida = ""

    while opcion_elegida not in lista_opciones:
        print("*" * 79)
        print("Que quieres hacer a continuación:")
        print("-" * 79)
        print("     1- Leer receta.")
        print("     2- Escribir receta.")
        print("     3- Crear categoria de recetas.")
        print("     4- Eliminar receta.")
        print("     5- Eliminar categoria.")
        print("     6- Salir del programa.")
        print("*" * 79)
        opcion_elegida = input("Opción: ")
        system("cls")

    match opcion_elegida:
        case "1":
            accion = "leer"
            categoria_elegida = elegir_categoria(accion)
            leer_receta(categoria_elegida)
        case "2":
            accion = "escribir"
            categoria_elegida = elegir_categoria(accion)
            escribir_receta(categoria_elegida)
        case "3":
            crear_categoria_receta()
        case "4":
            accion = "eliminar"
            categoria_elegida = elegir_categoria(accion)
            eliminar_receta(categoria_elegida)
        case "5":
            eliminar_categoria_receta()

    return opcion_elegida


def presiona_enter():
    print("*" * 79)
    input("Presione 'ENTER' para continuar")
    system("cls")


def elegir_categoria(accion):
    ruta = os.getcwd()
    # lista_categorias = list(filter(os.path.isdir, os.listdir(ruta)))
    lista_categorias = list(Path(ruta).iterdir())
    contador = 1
    categoria_elegida = "-1"

    while not categoria_elegida.isnumeric() or int(categoria_elegida) not in range(1, contador):
        contador = 1
        print("*" * 79)
        print(f"¿A qué categoria pertenece la receta que quieres {accion}?")
        print("-" * 79)
        for categoria in lista_categorias:
            print(f"        {contador}- {categoria.name}")
            contador += 1
        print("*" * 79)
        categoria_elegida = input("Categoria: ")

        system("cls")

    return lista_categorias[int(categoria_elegida)-1].name


def mostrar_recetas(ruta, contador):
    lista_recetas = []

    for txt in Path(ruta).glob("**/*.txt"):
        lista_recetas.append(txt.stem)
        print(f"    {contador}- {txt.stem}")
        contador += 1

    return lista_recetas, contador


def categoria_vacia():
    print("La categoria escogida no contiene recetas.")
    presiona_enter()


def leer_receta(categoria):
    ruta = os.getcwd()
    os.chdir(f"{ruta}\\{categoria}")
    ruta = os.getcwd()

    contador = 1
    receta_elegida = "-1"

    print("*" * 79)
    print(f"Categoria elegida: {categoria}")
    print("Estas son las recetas guardadas, cual quieres leer?")
    print("-" * 79)
    lista_recetas, contador = mostrar_recetas(ruta, contador)

    if len(lista_recetas) >= 1:
        while not receta_elegida.isnumeric() or int(receta_elegida) not in range(1, contador):
            print("*" * 79)
            receta_elegida = input("Receta: ")
            system("cls")

        receta_elegida = lista_recetas[int(receta_elegida) - 1]
        print("*" * 79)
        print(f"Receta elegida: {receta_elegida}")
        print("-" * 79)
        texto = open(f"{ruta}\\{receta_elegida}.txt", "r")
        contenido_receta = texto.read()
        print(contenido_receta)
        texto.close()
        presiona_enter()
    else:
        categoria_vacia()


def escribir_receta(categoria):
    ruta = os.getcwd()
    os.chdir(f"{ruta}\\{categoria}")
    ruta = os.getcwd()

    print("*" * 79)
    print(f"Categoria elegida: {categoria}\n")
    print("-" * 79)
    nombre = input("¿Cual va a ser el nombre de la receta que quieres guardar?\n")
    archivo = open(f"{ruta}\\{nombre}.txt", "w+")
    texto_receta = input("Escribe la nueva receta:\n")
    archivo.write(texto_receta)
    archivo.close()
    print("*" * 79)
    print("¡¡Receta creada!!")
    presiona_enter()


def crear_categoria_receta():
    print("*" * 79)
    print(f"Agregar categoria nueva de recetas\n")
    print("-" * 79)
    nombre = input("¿Cual va a ser el nombre de la nueva categoria?\n").upper()
    os.mkdir(nombre)
    print("*" * 79)
    print("¡¡Categoria creada!!")
    presiona_enter()


def eliminar_receta(categoria):
    ruta = os.getcwd()
    os.chdir(f"{ruta}\\{categoria}")
    ruta = os.getcwd()

    contador = 1
    receta_elegida = "-1"

    print("*" * 79)
    print(f"Categoria elegida: {categoria}")
    print("Estas son las recetas guardadas, cual quieres eliminar?")
    print("-" * 79)
    lista_recetas, contador = mostrar_recetas(ruta, contador)

    if len(lista_recetas) >= 1:
        while not receta_elegida.isnumeric() or int(receta_elegida) not in range(1, contador):
            print("*" * 79)
            receta_elegida = input("Receta: ")

        receta_elegida = lista_recetas[int(receta_elegida) - 1]
        os.remove(f"{ruta}\\{receta_elegida}.txt")
        print("*" * 79)
        print("¡¡Receta eliminada!!")
        presiona_enter()
    else:
        categoria_vacia()


def eliminar_categoria_receta():
    ruta = os.getcwd()
    lista_categorias = list(filter(os.path.isdir, os.listdir(ruta)))
    contador = 1
    categoria_elegida = "-1"

    while not categoria_elegida.isnumeric() or int(categoria_elegida) not in range(1, contador):
        contador = 1
        print("*" * 79)
        print(f"¿Que categoria es la que quieres eliminar??")
        print("-" * 79)
        for categoria in lista_categorias:
            print(f"        {contador}- {categoria}.")
            contador += 1
        print("*" * 79)
        categoria_elegida = input("Categoria: ")

    ruta = f"{ruta}\\{lista_categorias[int(categoria_elegida) - 1]}"
    for txt in Path(ruta).glob("**/*.txt"):
        os.remove(txt)
    os.rmdir(ruta)
    print("*" * 79)
    print("¡¡Categoria eliminada!!")
    presiona_enter()


"""
**********************************************************************
A PARTIR DE AQUI SE REALIZAN LAS LLAMADAS A LAS FUNCIONES DEL PROGRAMA
**********************************************************************
"""
ruta_inicio = creacion_carpetas_de_recetas()

bienvenida()

opcion_elegida = ""
while not opcion_elegida.isnumeric() or int(opcion_elegida) in range(1, 6):
    opcion_elegida = menu_de_inicio()
    ruta_inicial(ruta_inicio)

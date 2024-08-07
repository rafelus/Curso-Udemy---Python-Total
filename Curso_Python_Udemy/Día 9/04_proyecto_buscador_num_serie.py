"""
******************************************************************************************************
                    CODIGO PARA EXTRAER ARCHIVO DEL EJERCICIO DESDE UN .ZIP
import shutil

carpeta_destino = "C:\\Users\\rafa7\\OneDrive\\Documentos\\PycharmProjects\\Curso_Python_Udemy\\Día 9"
shutil.unpack_archive("Proyecto+Dia+9.zip",carpeta_destino, "zip")
******************************************************************************************************
"""
"""
Tu trabajo es crear un Buscador de Números de Serie. ¿Qué es eso? Es un programa que se encargue de buscar números
de serie que cumplan un determinado formato, dentro de un arbol de carpetas.

Tu programa va a recorrer todos los archivos y subcarpetas de un directorio raíz (en este caso, la carpeta que acabas
de descomprimir), y va a buscar cualquier string que coincida con un patrón de número de serie. Sabemos que no puede 
haber más de un número de serie por archivo.

Para lograrlo vas a usar el módulo os para abrir e iterar por el directorio, y las expresiones regulares para encontrar
el formato de número de serie correcto.

A los fines de este ejercicio, estas son las condiciones de formato que deben cumplir los hallazgos:
- [N] + [tres caracteres de texto] + [-] + [5 números]

Por ejemplo: Nryu-12365

La presentación en pantalla de los hallazgos debe ser un listado en formato de tabla, que respete el siguiente formato
de ejemplo:

----------------------------------------------------
Fecha de búsqueda: [fecha de hoy]

ARCHIVO		NRO. SERIE
-------		----------
texto1.txt	Nter-15496
texto25.txt	Ngba-85235

Números encontrados: 2
Duración de la búsqueda: 1 segundos
----------------------------------------------------

IMPORTANTE

* La 'Duración de búsqueda' debe estar redondeada hacia arriba

* No olvides que la mejor forma de recorrer un arbol de carpetas, probablemente sea con el método walk() de os.

* Observa que la fecha de búsqueda debe ser la fecha del día en que ejecutes el código, por lo que necesitas echar mano
del módulo datetime.

* Animate a encontrar una manera de mostrar la fecha de hoy con el formato dd/mm/aa.

* Para informar la duración de la búsqueda al final de tu presentación, vas a necesitar del módulo time.

* Recuerda que para poder imprimir todo en formato de tabla puedes usar los caracteres especiales \t para tabular.
"""
import os
import datetime
import re
import time
import math


def buscador_num_serie(texto):
    patron = r"N\D{3}-\d{5}"

    for frase in texto.readlines():
        verificacion = re.findall(patron, frase)
        if verificacion:
            texto.close()
            return verificacion[0]
    texto.close()
    return None


def imprimir_num_serie(lista_archivos):
    fecha_hoy = datetime.date.today()
    print("-" * 40)
    print(f"Fecha de búsqueda: {fecha_hoy.day}/{fecha_hoy.month}/{fecha_hoy.year}\n")
    print("ARCHIVO\t\t\t\t\tNRO. SERIE")
    print("-------\t\t\t\t\t----------")

    for archivo in lista_archivos:
        print(archivo)

    print(f"\nNúmeros encontrados: {len(lista_archivos)}")


def inicio():
    ruta_home = os.getcwd()
    ruta_busqueda = f"{ruta_home}\\Mi_Gran_Directorio"
    lista_arch = list()

    temp_inicio = time.time()
    for carpeta, subcarpeta, archivo in os.walk(ruta_busqueda):
        for arch in archivo:
            buscador = buscador_num_serie(open(f"{carpeta}\\{arch}", "r"))
            if buscador is not None:
                lista_arch.append(f"{arch}\t\t\t{buscador}")

    imprimir_num_serie(lista_arch)

    temp_final = time.time()
    temp_ejecucion = math.ceil(temp_final - temp_inicio)

    print(f"Duración de la búsqueda: {temp_ejecucion} segundos")
    print("-" * 55)


"""
*********************************************************************
                     AQUI EMPIEZA EL PROGRAMA
*********************************************************************
"""

inicio()

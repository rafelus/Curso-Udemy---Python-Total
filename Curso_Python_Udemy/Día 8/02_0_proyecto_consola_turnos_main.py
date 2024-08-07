"""
En nuestro caso, vas a crear el tunero para una farmacia que tiene tres áreas de atención:
perfumería, farmacia (que es donde venden los medicamentos), y cosméticos. Tu programa le
tiene que preguntar al cliente a cuál de las áreas desea dirigirse, y le va a dar un número de
turno según a qué área se dirija. Por ejemplo, si elige cosmética le va a dar el número C-54
(“C” de cosmética). Luego de eso, nos va a preguntar si queremos sacar otro turno. Esto, en
realidad, es para simular si viene un nuevo cliente. Y repetirá todo el proceso.
Algunas cosas a tener en cuenta:
Los diferentes clientes van a ir sacando turnos para diferentes áreas (perfumería, farmacia,
cosmética), en diferentes órdenes, por lo que el sistema debe llevar la cuenta de cuántos turnos
ha dado para cada una de esas áreas, y producir el siguiente número de cada área a medida
que se lo pida. ¿No te parece genial aprovechar la eficiencia de los generadores para poder
hacer esto?
Por otro lado, el mensaje donde le comunicamos el número de espera al cliente, debería tener
algo de texto adicional antes y después del número. Por ejemplo, “su turno es (-el número de
turno con el del comienzo-)”, y luego algo así como “aguarde y será atendido”. Para que
nuestro código no se repita, en vez de poner ese texto en cada una de las funciones que calculen
los números, podemos aprovechar la flexibilidad de los decoradores para crear ese texto
adicional una sola vez, y luego envolver a cualquiera de nuestras funciones con ese texto único.

"""
from proyecto_consola_turnos_numeros import *


def inicio():
    opcion = 0

    print("*" * 79)
    print("Bienvenido a la Farmacia Virtual")
    print("*" * 79)

    while opcion != 4:
        print("_" * 79)
        print("Escoja un departamento")
        print("_" * 79)
        print("     1 - Perfumería.")
        print("     2 - Farmacia.")
        print("     3 - Cosmética.")
        print("     4 - Salir")
        print("_" * 79)

        while True:
            try:
                opcion = int(input("Opción : "))
                [1, 2, 3].index(opcion)
                break
            except ValueError:
                print("Opción no válida")

        decorador_ticket(opcion)


"""
*********************************************************************
                     AQUI EMPIEZA EL PROGRAMA
*********************************************************************
"""

inicio()

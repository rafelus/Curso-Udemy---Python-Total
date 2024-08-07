"""El programa va a elegir una palabra secreta y le va a mostrar al jugador solamente una serie
de guiones que representa la cantidad de letras que tiene la palabra. El jugador en cada turno
deberá elegir una letra y si la letra se encuentra en la palabra oculta, el sistema le va a
mostrar en qué lugares se encuentra. Pero si el jugador dice una letra que no se encuentra en
la palabra oculta, pierde una vida.
En el juego real del ahorcado, cada vez que perdemos una vida, se va completando el dibujo
del ahorcado miembro por miembro. Pero en nuestro caso, como aún no tenemos elementos
gráficos, simplemente le vamos a decir que tiene seis vidas y se las iremos descontando de una
en una, cada vez que el jugador elija una letra incorrecta.
Si se agotan las vidas antes de adivinar la palabra, el jugador pierde. Pero si adivina la palabra
completa antes de perder todas las vidas, el jugador gana.
Parece sencillo, pero ¿cómo diseñamos todo este código? Bueno, aquí van algunas ayudas:
 Primero vas a crear un código que importe el método choice, ya que lo vas a necesitar
para que el sistema pueda elegir una palabra al azar dentro de una lista de palabras que
también vas a crear al comienzo.
 Luego de eso, vas a crear tantas funciones como creas necesarias para que el programa
haga cosas como pedirle al usuario que elija una letra, para corroborar si lo que el usuario
ha ingresado es una letra válida, para chequear si la letra ingresada se encuentra en la
palabra o no, para verificar si ha ganado o no, etc.
 Recuerda escribir primero las funciones y luego el código que las implementa
ordenadamente. """

from random import choice


def lista_palabras ():
    lista = ["Ajedrez","Caballo","Municipio","Ordenador","parrilla","vehiculo","cabaña","arbusto",
             "Castillo","rotulador","panadero","tiburon","helipuerto","dinosaurio"]
    return choice(lista)


def tablero_juego(palabra_secreta):
    tablero_nuevo = []
    for caracter in palabra_secreta:
        tablero_nuevo.append("_")
    return tablero_nuevo


def comprobar_caracter(letra_elegida, palabra_secreta, vidas, tablero):
    if letra_elegida in tablero:
        vidas -= 1
    elif letra_elegida in palabra_secreta:
        contador = 0
        for char in palabra_secreta:
            if letra_elegida == palabra_secreta[contador]:
                tablero[contador] = palabra_secreta[contador]
            contador += 1
    else:
        vidas -= 1
    return vidas, tablero


def juego_ahorcado():
    palabra_secreta = lista_palabras().upper()
    tablero = tablero_juego(palabra_secreta)
    vidas = 6

    while vidas != 0 and list(palabra_secreta) != tablero:
        print(f"Tienes {vidas} vidas, elige con cuidado\n")
        print(tablero)
        intento = ""
        while len(intento) != 1:
            intento = input("Elige una letra: ").upper()
        vidas, tablero = comprobar_caracter(intento, palabra_secreta, vidas, tablero)
    if list(palabra_secreta) == tablero:
        print(f"\n{tablero}\n¡¡¡Enorabuena has acertado la palabra secreta!!!")
    else:
        print(f"\n!!Te has quedado sin vidas¡¡\nLa palabra secreta era "
              f"'{palabra_secreta.strip()}', más suerte la próxima vez!")


print("Vamos a jugar al juego del ahorcado, intenta adivinar la palabra "
      "secreta antes de que se agoten todas tus vidas\n")
juego_ahorcado()
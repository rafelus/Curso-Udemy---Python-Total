#Ejercicio 1
class Mascota:
    def __init__(self):
        pass

    @staticmethod
    def respirar():
        print("Inhalar... Exhalar")

#Ejercicio 2
class Jugador:
    vivo = False
    def __init__(self):
        pass

    @classmethod
    def revivir(cls):
        Jugador.vivo = True

#Ejercicio 3
class Personaje:
    def __init__(self, cantidad_flechas):
        self.cantidad_flechas = cantidad_flechas

    def lanzar_flecha(self):
        self.cantidad_flechas -= 1
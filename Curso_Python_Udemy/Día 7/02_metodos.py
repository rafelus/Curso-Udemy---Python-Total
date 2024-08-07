#Ejercicio 1
class Perro:
    def __init__(self):
        pass
    def ladrar(self):
        print("Guau!")

mi_perro = Perro()
mi_perro.ladrar()

#Ejercicio 2
class Mago:
    def __init__(self):
        pass
    def lanzar_hechizo(self):
        print("¡Abracadabra!")

merlin = Mago()
merlin.lanzar_hechizo()

#Ejercicio 3
class Alarma:
    def __init__(self):
        pass
    def postergar(self, cantidad_minutos):
        print(f"La alarma ha sido pospuesta {cantidad_minutos} minutos")
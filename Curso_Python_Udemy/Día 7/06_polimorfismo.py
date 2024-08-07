#Ejercicio 1
palabra = "polimorfismo"
lista = ["Clases", "POO", "Polimorfismo"]
tupla = (1, 2, 3, 80)

print(len(palabra))
print(len(lista))
print(len(tupla))
#Ejercicio 2
class Mago():
    def atacar(self):
        print("Ataque mágico")

class Arquero():
    def atacar(self):
        print("Lanzamiento de flecha")

class Samurai():
    def atacar(self):
        print("Ataque con katana")

arquero = Arquero()
mago = Mago()
samurai = Samurai()

personajes =[arquero.atacar(), mago.atacar(), samurai.atacar()]

#Ejercicio 3
class Mago():
    def defender(self):
        print("Escudo mágico")

class Arquero():
    def defender(self):
        print("Esconderse")

class Samurai():
    def defender(self):
        print("Bloqueo")

mago = Mago()
arquero = Arquero()
samurai = Samurai()

def personaje_defender(personaje):
    personaje.defender()
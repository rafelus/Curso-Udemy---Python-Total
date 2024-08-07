#Ejercicio 1
def abrir_leer(archivo):
    texto = open(archivo, "r")
    return texto.read()

print(abrir_leer("registro.txt"))
#Ejercicio 2
def sobrescribir(archivo):
    texto = open(archivo, "w")
    texto.write("contenido eliminado")

sobrescribir("mi_archivo.txt")
#Ejercicio 3
def registro_error(archivo):
    texto = open(archivo, "a")
    texto.write("\nse ha registrado un error de ejecución")
    texto.close()

registro_error(("mi_archivo.txt"))
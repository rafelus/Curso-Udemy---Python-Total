#Ejercicio 1
import re

def verificar_email(email):
    patron = r"@\w+\.com"
    comprobacion = re.search(patron, email)
    if comprobacion:
        print("Ok")
    else:
        print("La dirección de email es incorrecta")
#Ejercicio 2

def verificar_saludo(frase):
    patron = r"^Hola"
    comprobacion = re.search(patron, frase)
    if comprobacion:
        print("Ok")
    else:
        print("No has saludado")
#Ejercicio 3

def verificar_cp (cp):
    patron = r"\w{2}\d{4}"
    comprobacion = re.search(patron, cp)
    if comprobacion:
        print("Ok")
    else:
        print("El código postal ingresado no es correcto")
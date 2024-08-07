import bs4
import requests

resultado = requests.get("https://www.escueladirecta.com/courses/")

sopa = bs4.BeautifulSoup(resultado.text, "lxml")

"""print(sopa.select("title"))
print(sopa.select("title")[0].getText())

parrafo_esp = sopa.select("p")[3].getText()

print(parrafo_esp)

columna_later = sopa.select(".title")

print(columna_later)"""

imagenes = sopa.select(".course-box-image")[0]["src"]

print(imagenes)

imagen_curso = requests.get(imagenes).content

"""f = open("mi_imagen.jpg", "wb")
f.write(imagen_curso)
f.close()"""

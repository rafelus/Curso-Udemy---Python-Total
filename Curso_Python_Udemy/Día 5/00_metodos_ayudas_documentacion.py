#Ejercicio 1
string = ",:_#,,,,,,:::____##Pyt%on_ _Total,,,,,,::#"
print(string.lstrip(",").lstrip(":").lstrip("%").lstrip("_").lstrip("#").lstrip(",").lstrip(":").lstrip("_").lstrip("#"))
#Ejercicio 2
frutas = ["mango", "banana", "cereza", "ciruela", "pomelo"]
frutas.insert(3, "naranja")
#Ejercicio 3
marcas_smartphones = {"Samsung", "Xiaomi", "Apple", "Huawei", "LG"}
marcas_tv = {"Sony", "Philips", "Samsung", "LG"}
conjuntos_aislados = marcas_smartphones.isdisjoint(marcas_tv)
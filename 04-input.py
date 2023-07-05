# Además de expulsar valores, datos o información, los programas reciben valores que de alguna forma manipulan y transforman. Python trae una función incorporada llamada input, que permite ingresar datos o valores al programa.
print("Hola, dime cuál es tu nombre ")
name = input()
print("Hola"+name)
print("¿Cuantos años tienes?")
# Una caracteristica de la función input es que solo entrega texto.
age = input()
print(type(age))
print("Naciste en" + "2023"-age)
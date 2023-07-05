# Para salir del loop bajo cierta condición, podemos utilizar la estructura de control if junto con la palabra clave break.

for letter in "murcielago":
    print(letter)
    if letter == "a":
        break
print("Esto es después del loop")
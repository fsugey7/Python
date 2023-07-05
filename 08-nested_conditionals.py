
# Una evaluación condicional puede estar dentro de otra. Por ejemplo:

name = input("Hola. cúal es tu nombre")
age = int(input("Dime tu edad"))

print("Hola", name, "!")

if(age >= 18):
    drink = input("¿Quieres cerveza o vino?")
    if(drink) == "cerveza":
        print("Toma : ")
        print("Aquí tienes tu cerveza")
    else:
        print("Aquí tienes tu vino")
else:
    juice = input("¿Quieres jugo de frutilla o naranja?")
    if(juice == "Frutilla" or juice == " Naranja"):
        print("Acá está tu jugo de fresas")
    else:
        print("Toma tu jugo de naranja")
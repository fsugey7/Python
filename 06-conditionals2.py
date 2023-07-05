# Las expresiones boolenas nos permite hacer flujos de ejecución condicional utilizando estructuras de control.

age = int(input("¿Cúal es tu edad?"))

if(age >= 18):
    print("Eres mayor de edad")
else: # El else no lleva expresion boolena
    print("Entonces eres menor de edad")
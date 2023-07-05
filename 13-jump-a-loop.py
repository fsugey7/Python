# Podemos saltar una iteración usando la palabra clave continue.

for letter in "murcielago":
    if letter == "l":
        continue
    print(letter)

print("----------------")
for letter in "banana":
    if letter == "a":
        continue
    print(letter)
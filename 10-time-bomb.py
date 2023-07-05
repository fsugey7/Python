import time
# Ejercicio: hacer un programa que parta contando regresivamente desde 10 y que al llegar a 0 diga "Boom".
# Tip: esperar un segundo entre cada interacción utilizando time.sleep(1).

# 10
# 9 
# 8 
# ...
# Boom
num = 10
while num >= 0:
    print(num)
    num = num - 1
    time.sleep(1)
    
print("Booom")
print(num)
from random import randint

x = randint (-99,99)

def verificador (x):
    if x > 0:
        return "P"
    if x <= 0:
        return "N"

print(verificador(x))

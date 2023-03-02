x = int(input("digite quantos digitos quiser"))
def contador(x):
    if x < 0:
        x = x * -1
    contador = 0
    for i in range(len(str(x))):
        contador +=1
    return contador

num = contador(x)
print(num)
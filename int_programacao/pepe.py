preco = 0
dicionario = {"latas": 0,"litros": 0 }
litros = int(input("digite a quantidade de litros"))

while(litros > 0):
    if litros >= 10:
        dicionario["latas"] =  dicionario["latas"] + 1
        preco += 50
        litros -= 10
    elif litros > 0:
        dicionario["litros"] = dicionario["litros"] + 1
        preco += 5.5
        litros -= 1

print(preco)
input("")
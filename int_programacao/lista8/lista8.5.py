frase = input("digite a frase que voce quer saber")
caract = "abcdefghijklmnopqrstuvwxyz"
contador = 0
lista = []
for i in range (len(caract)):
    for j in range (len(frase)):
        if frase[j] == caract[i]:
            contador += 1
    lista.append(caract[i])
    lista.append(contador)
    contador = 0
print(lista)
#infelizmente não consegui fazer um dicionario da forma correta então decidi deixar assim mesmo
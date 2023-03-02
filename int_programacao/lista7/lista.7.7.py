frase = ''
lista_frase = []
lista_dicionario = []
frase = input('Digite a frase: ')

while (frase != '-1'):
    dicionario = {}

    for caracter in frase:
        contador = 0
        
        for caract in frase:
            if caract == caracter:
                contador += 1
        dicionario[caracter] = contador
    lista_dicionario.append(dicionario)
    lista_frase.append(frase)

    frase = input('Digite a frase ou -1 pra sair: ')

for i in range(len(lista_frase)):
    print(lista_frase[i])
    print(lista_dicionario[i])
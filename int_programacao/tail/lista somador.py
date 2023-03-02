lista = [3,5,14,27,13,2,9,4,6,2,1]
somador = False 
k = int(input("Digite um numero para saber se tem 2 numeros que dão esse numero: "))
for i in range(len(lista)):   
    if somador == True:
        break 
    for j in range(len(lista)):
        if lista[i] + lista[j] == k and lista[i] != lista[j]:
            print ("para o valor =",k,"esse são os 2 valores da lista que dão eles",lista[j], "+",lista[i])
            somador = True  
if somador == False:
    print("não tem numeros para dar esse valor")
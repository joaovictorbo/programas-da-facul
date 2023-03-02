lista1 = [1, 4, 5, 2, 7,] 
lista2 = [3, 8, 9, 11, 13] 
lista = lista1 + lista2 
lista[::2] = lista1 
lista[1::2] = lista2 
print ("a lista intercalada é: ",lista) 
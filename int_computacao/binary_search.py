# -*- coding: utf-8 -*-

from random import randint
tamanho = 100
def binary_search(arr, x):
    pequeno = 0
    tamanho = len(arr) - 1
    mid = 0
 
    while pequeno <= tamanho:
 
        mid = (tamanho + pequeno) // 2
 
        
        if arr[mid] < x:
            pequeno = mid + 1
 
       
        elif arr[mid] > x:
            tamanho = mid - 1
 
        
        else:
            return mid
 
    
    return -1
    




v = [randint(0,tamanho) for i in range(tamanho)]


v.sort()
print(v)


pos = binary_search(v, 11)
if(pos >= 0):
    print("Achei na posição:" + str(pos))
else:
    print("O elemento não está no vetor!")


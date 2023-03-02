from random import randint
from threading import Thread

tamanho = 1000000
 
v = [randint(0,tamanho) for i in range(tamanho)]
def achar_maior():
    
    maior = 0 
    
    for num in (v):

        if num > maior:
            maior = num
    
    return maior
maior = achar_maior()

x = Thread(target=achar_maior())
x.start()



x.join()
print (maiorm) 

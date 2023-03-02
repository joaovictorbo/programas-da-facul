from random import randint
from threading import Thread
tamanho = 1000000
list1 = [randint(0,tamanho) for i in range(tamanho)]
def myMax():
    max = list1[0]
    for x in list1:
        if x > max :
             max = x
    return max



mymax = myMax()
print(mymax)




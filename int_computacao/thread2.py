from random import randint
from threading import Thread

tamanho = 1000000

million = [randint(0,tamanho) for i in range(tamanho)]

#List slice, I'm just cutting in half pieces
list1 = million[500000:]
list2 = million[:500000]

# There is some reason to use list instead of commmon vars
# 1st reason: If we use common variable, we couldn't recycle myMax function to be
# used with both threads(main and thd).

# Há algum motivo para usar list em vez de vars comuns
# 1º motivo: Se usarmos a variável comum, não poderíamos reciclar a função myMax para ser
# usado com ambas as threads (main e thd).
c_max = [0]*2 


#idx argument will be used to change what c_max var we'll put our results

#O parâmetro idx será usado para alterar qual variável c_max colocaremos nossos resultados
def myMax(v, idx):
    for x in v:
        if x > c_max[idx] :
             c_max[idx] = x

thd = Thread(target=myMax, args=(list2,1)) 
thd.start()

myMax(list1, 0)

#Wait thd finish it work

#Espera thd terminar seu trabalho
thd.join() 

#Yeah this is a conditional expression under a function
#We can use it to set different values to be sended through functions, small stuff

#Sim, esta é uma expressão condicional dentro de uma função
#Podemos usá-lo para definir valores diferentes a serem enviados através de funções, coisa pequena
print(c_max[0] if c_max[0] > c_max[1] else c_max[1])


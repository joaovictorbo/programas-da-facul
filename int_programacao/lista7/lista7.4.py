from random import randint

jogadas = []
while True:
    n = int(input("digite a quantidade de dados"))
    if n == 0:
        break
    for i in range (n):
        jogadas.append(randint(1,6))
    lado1 = 0
    lado2 = 0
    lado3 = 0
    lado4 = 0
    lado5 = 0
    lado6 = 0

    
    for i in range( len(jogadas)):
        if jogadas[i] == 1:
            lado1 += 1
        elif jogadas[i] == 2:
            lado2 += 1
        elif jogadas[i] == 3:
            lado3 += 1
        elif jogadas[i] == 4:
            lado4 += 1
        elif jogadas[i] == 5:
            lado5 += 1
        else:
            lado6 += 1


    print ((lado1*100)//len(jogadas),"%",(lado2*100)//len(jogadas),"%",(lado3*100)//len(jogadas),"%",(lado4*100)//len(jogadas),"%",(lado5*100)//len(jogadas),"%",(lado6*100)//len(jogadas),"%")
    jogadas = []
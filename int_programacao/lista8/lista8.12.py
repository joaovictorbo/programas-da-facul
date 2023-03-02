x = int(input("digite um numero"))
def funcao(x):
    for i in range(x+1):
        print()
        for j in range (i):
            print(i, end=" ")

funcao(x)
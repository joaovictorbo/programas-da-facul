caminho = input("digite o caminho do aspirador de pó") 
d = 0
e = 0
c = 0 
b = 0 
inicio = False 
for i in range(len(caminho)):
    if caminho[i] == "D":
        d += 1
    if caminho[i] == "C":
        c += 1
    if caminho[i] == "E":
        e += 1    
    if caminho[i] == "B":
        b += 1
if (e - d) == 0 and (c - b) == 0:
    print("o robo vai voltar para o inicio")
    inicio = True
if inicio == False:
    print("ele não volta pro inicio ")
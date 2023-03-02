numcll = input("digite o numero do seu celular: ") 
boleano = False
for i in range (len(numcll)):
    if numcll[i] == "-":
        boleano = True 
if len(numcll) == 8:
    numcll = "9"+numcll
if len(numcll) == 9 and boleano == True:
    numcll = "9"+numcll
elif len(numcll) == 9:
    numcll1 = numcll [5:]
    numcll2 = numcll[:5]
    numcll = numcll2 + "-" + numcll1
print (numcll)
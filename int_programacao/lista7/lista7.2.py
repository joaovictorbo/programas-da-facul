matriz = [[None]*3 for i in range (3)]
auxiliar = [0]

for i in range(3):
    for j in range(3):
        matriz[i][j] = int(input('Digite o valor do elemento [%d][%d]: ' % (i, j)))

            
auxiliar = matriz[1][2] 
matriz [1][2] = matriz[2][1]
matriz[2][1] = auxiliar

auxiliar = matriz[0][1] 
matriz [0][1] = matriz[1][0]
matriz[1][0] = auxiliar



print (matriz)
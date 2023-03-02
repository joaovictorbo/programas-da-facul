x = 1
matriz = [[None] * 10 for _ in range (2)]
for i in range (2):
    for j in range (10):
        if i == 0:
            matriz[i][j] = int(input("digite as altura e quando o contador resetar digite os sexos [%d]: "  % (j)))
        if i == 1:
            matriz[i][j] = input("digite as altura e quando o contador resetar digite os sexos [%d]: "  % (j))
print(matriz)
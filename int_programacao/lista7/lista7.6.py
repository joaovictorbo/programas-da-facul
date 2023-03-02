n = int(input("Digite a quantidade de pontos que deseja informar: "))
d = 0
distancia_media = 0

lista = []
lista_max = -999999.9
lista_min = 99999.9
for i in range(0,n):
    x = int(input("X: "))
    y = int(input("Y: "))
    lista.append((x,y))

lista_resultados = []

contador = 0
for i in range(n):
    contador += 1
    for j in range(contador,n):
        calculo_euclidiano = ( ((lista[i][0]- lista[j][0]) **2) + ((lista[i][1]- lista[j][1]) **2) ) **0.5
        lista_resultados.append(calculo_euclidiano)
        d = d + 1
for k in range(d):
    distancia_media = distancia_media + lista_resultados[k]
distancia_media = distancia_media / d

for j in range(len(lista_resultados)):
    if lista_resultados[j] > lista_max:
        lista_max = lista_resultados[j]

for p in range(len(lista_resultados)):
    if lista_resultados[p] < lista_min:
        lista_min = lista_resultados[p]




print(" A distancia maxima entre dois pontos e ",(lista_max))
print(" A distancia minima entre dois pontos e ",(lista_min))
print(" A distancia media entre dois pontos e ",distancia_media)
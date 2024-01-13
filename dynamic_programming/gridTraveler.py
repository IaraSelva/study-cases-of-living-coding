# você está viajando em um grid 2D de tamanho x,y
# partindo do ponto superior esquerdo, quantos caminhos são possíveis até chegar no ponto inferior direito
# num grid de tamano 2,3 por exemplo -> ao andar para o lado horizontalmente, 
# os caminhos se reduzem e podemos dizer que o grid tem agora tamanho 1,2
# Andando 1 verticalmente, podemos reduzir o grid ao tamanho 1,1 e assim chegamos no ponto final
# Ao chegarmos num ponto em que uma das coordenadas seja zero, como 1,0 ou 0,1 não é possível avançar então só retornamos zero


def gridTravel(x, y, table = {}):
    key = str(x) + "," + str(y)
    if key in table: return table[key]
    
    if x == 0 or y == 0 : return 0
    if x == 1 and y == 1: return 1

    table[key] = gridTravel(x-1, y, table) + gridTravel(x, y-1, table)

    return table[key]

print(gridTravel(1,1))
print(gridTravel(2,3))
print(gridTravel(3,2))
print(gridTravel(3,3))
print(gridTravel(18,18))

    

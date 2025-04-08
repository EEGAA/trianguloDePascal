#Este Codigo solo muestra los triangulos. no implementa El juego de la vida
import pygame
import numpy as np
import time
pygame.init()
ancho, alto = 555, 555
pantalla = pygame.display.set_mode((alto, ancho))
bg = 25, 25, 25
pantalla.fill(bg)

nxC, nyC = 100, 100
dimCW = ancho / nxC
dimCH = alto / nyC

gameState = np.zeros((nxC, nyC))
def TOT(dim):
    tot = 0
    for i in range(1, dim + 1):
        tot += i
    return tot

def pascal(dim):
    tot = TOT(dim)
    dta = np.zeros(tot)
    print(" dim =", dim, "tot =", tot, "\n")
    #print(dta)
    #Logica Pascal
    for cont in range(1, dim+1):
        if cont > 2:
            for i in range(cont-2):
                aux[1, i+1] = aux[0, i] + aux[0, i+1]
            for i in range(cont):
                pos += 1
                dta[pos] = aux[1, i]
                aux[0, i] = aux[1, i]
        else:
            if cont == 1:
                pos = 0
                nuevo = 1
                dta[pos] = nuevo
            else:
                for i in range(2):
                    pos += 1
                    dta[pos] = nuevo
            aux = np.ones((2, dim))
    #print(dta)
    return dta


def viewTRI(dim, dta, mul):
    print("mul =", mul, end="")
    pos = -1
    cont = 1
    aux = int(nxC/4)
    auy = 0
    
    for y in range(dim):
        for x in range(cont):
            pos += 1
            if dta[pos] % mul == 0:
                gameState[x+aux, y+auy] = 1
        cont += 1

def trabajo(dim, mul):#filas del triangulo, multiplos de...
    viewTRI(dim, pascal(dim), mul)

k = 1
#pausa = False
for k in range (1, 30):
    pantalla.fill(bg)
    gameState = np.zeros_like(gameState)
    trabajo(55, k)
    #newGameState = np.copy(gameState)
    for y in range(0, nxC):
        for x in range(0, nyC):
            poly = [((x)   * dimCW, (y)   * dimCH),
                    ((x+1) * dimCW, (y)   * dimCH),
                    ((x+1) * dimCW, (y+1) * dimCH),
                    ((x)   * dimCW, (y+1) * dimCH)]
            if gameState[x, y] == 0:
                pygame.draw.polygon(pantalla, (128, 128, 128), poly, 1)
            else:
                pygame.draw.polygon(pantalla, (255, 255, 255), poly, 0)
    pygame.display.flip()
    time.sleep(1.3)
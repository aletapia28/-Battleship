from ast import Return
import csv
import time
import os
import random

from utils import *


def readFile(fileName):
    with open("{}.txt".format(fileName), newline='') as file:
        ships = csv.reader(file, delimiter=',')
        boatIndex = 0
        for boat in ships:
            processPosition(boat, computerGrid, SHIPS[boatIndex][0])
            boatIndex += 1


def validateBoatPosition(boat):
    isValid = True
    for pos in boat:
        isValid = validateRowColumn(pos)
        if not isValid:
            return False
    return True


def validateRowColumn(pos):
    row, col = getRowColumn(pos)

    if(not row.upper() in ROWS):
        print('La fila {} de {}{} no es valida'.format(row, row, col))
        print('Intente de nuevo')
        print("\n\n--------------------------------------------------")

        return False
    elif(not col.isnumeric() or int(col) > GRID_SIZE-1):
        print('La columna {} de {}{} no es valida'.format(col, row, col))
        print('Intente de nuevo')
        print("\n\n--------------------------------------------------")
        return False
    else:
        return True


def processPosition(shipPosition, grid, mark):
    for pos in shipPosition or []:
        placePosition(pos, grid, mark)


def placePosition(pos, grid, mark):
    row, col = getRowColumn(pos)
    rowIndex = ROWS.index(row.upper())
    grid[int(rowIndex)][int(col)] = mark #SHIPS[boat][0]


def getRowColumn(pos):
    try:
        return pos[0], pos[1:]
    except:
        return pos, ""


def getPlayerShips():
    index = 0
    while(index < len(SHIPS)):
        print('Digite las posiciones del {}'.format(SHIPS[index]))
        boat = input()
        validPositions = validateBoatPosition(boat.split(','))
        if(validPositions):
            processPosition(boat.split(','), playerGrid, SHIPS[index][0])
            index += 1


def shoot(pos, grid):
    isPositionValid = validateRowColumn(pos)
    if(isPositionValid):
        isShootValid, message = checkHit(pos,grid)
        if(isShootValid):
            placePosition(pos, grid, message)
            if(message == "O"):
                print( "Barco impactado en {}".format(pos))
                return isShootValid , "Barco impactado {}".format(pos)
            else:
                print ("Oceano impactado {}".format(pos))
                return isShootValid, "Oceano impactado {}".format(pos)
        else:
            print(message)
            return isShootValid, message
    return False,"Posicion no válida"

def getPosition(pos,grid):
    row, col = getRowColumn(pos)
    rowIndex = ROWS.index(row.upper())
    value = grid[int(rowIndex)][int(col)] 
    return value

def checkHit(pos,grid):
    pos = getPosition(pos,grid)
    if(pos == "#"): return True,"X"
    if(pos == "O"): return False,"Este barco ya ha sido impactado en esta casilla."
    if(pos == "X"): return False,"Esta casilla ya ha sido impactada."
    else: return True,"O"

def getRandomTarget():
    row = ROWS[random.randint(0,9)]
    col = random.randint(0,9)
    pos ="{}{}".format(row,str(col))
    print(pos)
    return "{}{}".format(row,str(col))

def computerShoot():
    isValid = False
    global pcHits
    while(not isValid):
        print("Digite las coordenadas de su disparo:")
        target = getRandomTarget()
        isValid, message = shoot(target, playerGrid)    
    if(checkHit(target,playerGrid)):
        pcHits = pcHits + 1

def playerShoot():
    isValid = False
    global playerHits
    while(not isValid):
        print("Digite las coordenadas de su disparo:")
        target = input()
        isValid, message = shoot(target, computerGrid)    
    if(checkHit(target,computerGrid)):
        playerHits = playerHits + 1

def getRandomStarter():
    starter = random.randint(0,10)
    if(starter % 2 == 0):
        print("La computadora empieza")
        return "computer","player"
    else:
        print("El jugador empieza")
        return "player","computer"

def checkIfWinner():
    if(playerHits == BOATS_UNITS):
        print("El jugador ha ganado")
        return True
    elif(pcHits == BOATS_UNITS):
        print ("La computadora ha ganado")
        return True
    return False


def game():
    existsWinner = False
    first, second = getRandomStarter()
    while not existsWinner:
        eval(first+'Shoot()')
        # printGame(playerGrid, computerGrid)
        printColorGrid(eval(second+'Grid'))
        time.sleep(1.5)
        eval(second+'Shoot()')
        printColorGrid(eval(first+'Grid'))
        # printGame(playerGrid, computerGrid)
        
        existsWinner = checkIfWinner()


def startGame():
    print("Welcome")
    global computerGrid
    global playerGrid
    global playerHits 
    global pcHits 
    playerGrid = buildGrid()
    computerGrid = buildGrid()
    playerHits = 0
    pcHits = 0
    file = readFile("ships")
    getPlayerShips()

    os.system('cls')


   




def battleShip():
    startGame()
    game()


battleShip()

# TODO:
# Obtener disparo de PC de manera eficiente
# Buscar empate
# Dar oportunidad de empate


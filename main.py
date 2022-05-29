import csv
import time
from colorama import Fore, init
init(convert=True)


from utils import *

def readFile(fileName):
    with open("{}.txt".format(fileName), newline='') as file:
        ships = csv.reader(file, delimiter=',')
        boatIndex = 0
        for boat in ships:
            processPosition(boat, boatIndex, computerGrid)
            boatIndex += 1


def validatePosition(boat):
    for pos in boat:
        row, col = getRowColumn(pos)
        if(not row.upper() in ROWS):
            print('La fila {} no es valida'.format(row))
            print('Intente de nuevo')
            print("\n\n--------------------------------------------------")

            return False
        elif(int(col) > GRID_SIZE-1):
            print('La columna {} no es valida'.format(col))
            print('Intente de nuevo')
            print("\n\n--------------------------------------------------")
            return False

    return True

def processPosition(shipPosition, boat, grid):
    for pos in shipPosition or []:
        row, col = getRowColumn(pos)
        placePosition(row, col, boat, grid)


def placePosition(row, col, boat, grid):
    rowIndex = ROWS.index(row.upper())
    grid[int(rowIndex)][int(col)] = SHIPS[boat][0]


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
        validPositions = validatePosition(boat.split(','))
        if(validPositions):
            processPosition(boat.split(','), index, playerGrid)
            index += 1


def startGame():
    print("Welcome")
    global computerGrid
    global playerGrid
    playerGrid = buildGrid()
    computerGrid = buildGrid()
    file = readFile("ships")
    getPlayerShips()
    printGame(playerGrid,computerGrid)


def play():
    return "Finish"


def battleShip():

    startGame()
    play()


battleShip()

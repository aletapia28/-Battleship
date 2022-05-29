import colorama
from colorama import Fore, init 
from vars import *


def printColorGrid(grid):
    for row in grid:
        print("")
        for col in row:
            if(col == "#"):
                print(Fore.BLUE + col, end=" ")
            else:
                print(Fore.GREEN + col, end=" ")

def buildGrid():
    return [["#"] * GRID_SIZE for i in range(GRID_SIZE)]


def printGrid(grid):
    for i in grid:
        print(i)

def printGame(playerGrid,computerGrid):
    printColorGrid(playerGrid)
    print("\n\n--------------------------------------------------")
    printColorGrid(computerGrid)



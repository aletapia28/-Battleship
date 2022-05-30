import colorama
from colorama import Fore, init 
from vars import *
init(convert=True)


def printColorGrid(grid):
    for row in grid:
        print("")
        for col in row:
            if(col == "#"):
                print(Fore.BLUE + col, end=" ")
            elif(col == "O"):
                print(Fore.WHITE + col, end=" ")
            elif(col == "X"):
                print(Fore.RED + col, end=" ")
            else:
                print(Fore.GREEN + col, end=" ")
    print(Fore.RESET)

def buildGrid():
    return [["#"] * GRID_SIZE for i in range(GRID_SIZE)]


def printGrid(grid):
    for i in grid:
        print(i)

def printGame(playerGrid,computerGrid):
    printColorGrid(playerGrid)
    print("\n\n--------------------------------------------------")
    printColorGrid(computerGrid)



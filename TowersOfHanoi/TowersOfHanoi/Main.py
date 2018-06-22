from HanoiGame import HanoiGame
from HanoiDraw import *
import os

def main():
    numberOfDisks = AskForNumberOfDisks()
    Game = HanoiGame(numberOfDisks)
    Drawer = HanoiDraw()
    Drawer.DrawStacks(Game)
    _game_procedur(Game, Drawer)
    print("WON")
   
def _game_procedur(Game, Drawer):
    while Game.CheckIfGameWon() is False:
            try:
                startStack = AskForStack("Start")
                endStack = AskForStack("End")
                clear = lambda: os.system('cls')
                clear()
                Game.turn(startStack, endStack)
                Drawer.DrawStacks(Game)
            except Exception as e:
                print('ERROR: ' + str(e))
                Drawer.DrawStacks(Game)
    return
   
def AskForNumberOfDisks():
    correctInput = False
    
    while correctInput is False:
        try:
            i = int(input("Number of Disks (2-10): "))
            if(i > 2 and i <= 10):
                return i
            else:
                 print("Wrong Input")
        except ValueError:
            print("Wrong Input")
               
def AskForStack(stackString):
    i = 0
    try:
        print("Please select the " + stackString )
        print("1[a] 2[b] 3[c]")
        i = int(input("INPUT: "))
    except Exception as e:
        print("Wrong Input")
    return i

if __name__ == "__main__": main()


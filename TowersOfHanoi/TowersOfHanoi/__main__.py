from hanoi import Hanoi
from draw import *
import os
def main():
    number_of_disks = AskForNumberOfDisks()
    game = Hanoi(number_of_disks)
    DrawStacks(game)
    game_procedur(game)
    print("WON")
   
def game_procedur(game):
    clear = lambda: os.system('cls')
    
    while game:
        try:
            start_stack = ask_for_stack("Start")
            end_stack = ask_for_stack("End")
            clear()
            game.turn(start_stack, end_stack)
            DrawStacks(game)
        except Exception as e:
            print('ERROR: ' + str(e))
            DrawStacks(game)
   
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
               
def ask_for_stack(stackString):
    i = 0
    try:
        print("Please select the " + stackString )
        print("1[a] 2[b] 3[c]")
        i = int(input("INPUT: "))
    except Exception as e:
        print("Wrong Input")
    if i is 1:
        return Stack.START
    if i is 2: 
        return Stack.HELPER
    if i is 3:
        return Stack.DESTINATION       

if __name__ == '__main__':
    main()


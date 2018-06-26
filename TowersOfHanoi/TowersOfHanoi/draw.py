from hanoi import *

def DrawStacks(game:Hanoi):

        stack1 = ConvertStack(game[Stack.START], game)
        stack2 = ConvertStack(game[Stack.HELPER], game)
        stack3 = ConvertStack(game[Stack.DESTINATION], game)

        #Draw Stacks
        for i in range(0, len(stack1)):
            DrawLine(stack1, stack1[i], "X")
            print(" ", end='')

            DrawLine(stack1, stack2[i], "X")
            print(" ", end='')

            DrawLine(stack1, stack3[i], "X")
            print(" ", end='')

            print()
            i+=1
        entireWith = len(stack1)*2-1
        #draw Bottom
        for i in range(0, 3):
            for j in range(0, entireWith):
                print("_", end='')
            print(" ", end='')
        print()

        #draw Letters
        empySpaceBeforeDisk1 = entireWith - len(stack1)
        for i in range(0,3):
            if i is 0:
                DrawLine(stack1, 1, "a")
                print(" ", end='')
            if i is 1:
                DrawLine(stack1, 1, "b")
                print(" ", end='')
            if i is 2:
                DrawLine(stack1, 1, "c")
                print(" ", end='')
        print()

def ConvertStack(stack : list, game : Hanoi):
    while len(stack) < game.num_disks:
        stack.append(0)
    stack.sort()
    return stack


def DrawLine(startStack: list, value: int, character):
        emtySpacesBefore = 0
        while emtySpacesBefore < len(startStack)- value:
            print(" ", end='')
            emtySpacesBefore +=1

        diskCharacter = 0
        while diskCharacter < value*2 -1:
            print(character, end='')
            diskCharacter += 1

        emtySpacesAfter = 0
        while emtySpacesAfter < (len(startStack)*2-1) - emtySpacesBefore - diskCharacter:
            print(" ", end='')
            emtySpacesAfter+=1


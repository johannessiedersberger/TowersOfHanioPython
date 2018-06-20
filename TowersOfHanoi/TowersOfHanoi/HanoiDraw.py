from HanoiGame import HanoiGame


def main():
    Game = HanoiGame(3)
    Game.turn(1,2)
    print(Game.ReturnStackCopied(1).items)
    print(Game._firstStack.items)
    
    
def DrawLine(self, startStack, value, character):
    emtySpacesBefore = 0
    while emtySpacesBefore < startStack.Count() - value:
        print(" ", end='')
        emtySpacesBefore +=1

    diskCharacter = 0
    while diskCharacter < value*2 -1:
        print(character, end='')
        diskCharacter += 1

    emtySpacesAfter = 0
    while emtySpacesAfter < (startStack.Count() *2-1) - emtySpacesBefore - diskCharacter:
        print(" ", end='')
        emtySpacesAfter+=1

def DrawStacks(self, Game ):
    for i in range(0,Game.ReturnStackCopied(1).Count()):
        return
    return
    



if __name__ == "__main__": main()
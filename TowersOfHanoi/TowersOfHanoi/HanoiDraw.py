from HanoiGame import HanoiGame
    
class HanoiDraw:

    def DrawLine(self, startStack, value, character):
        emtySpacesBefore = 0
        while emtySpacesBefore < startStack.size() - value:
            print(" ", end='')
            emtySpacesBefore +=1

        diskCharacter = 0
        while diskCharacter < value*2 -1:
            print(character, end='')
            diskCharacter += 1

        emtySpacesAfter = 0
        while emtySpacesAfter < (startStack.size() *2-1) - emtySpacesBefore - diskCharacter:
            print(" ", end='')
            emtySpacesAfter+=1

    def DrawStacks(self, Game ):
        for i in range(0,Game.ReturnStackCopied(1).size()):
            self.DrawLine(Game.ReturnStackCopied(1), Game.ReturnStackCopied(1).index(i), "X")
            print(" ", end='')

            self.DrawLine(Game.ReturnStackCopied(1), Game.ReturnStackCopied(2).index(i), "X")
            print(" ", end='')

            self.DrawLine(Game.ReturnStackCopied(1), Game.ReturnStackCopied(3).index(i), "X")
            print(" ", end='')

            print()
            i+=1
        entireWith = Game.ReturnStackCopied(1).size()*2-1
        #draw Bottom
        for i in range(0, 3):
            for j in range(0, entireWith):
                print("_", end='')
            print(" ", end='')
        print()

        #draw Letters
        empySpaceBeforeDisk1 = entireWith - Game.ReturnStackCopied(1).size()
        for i in range(0,3):
            if i is 0:
                self.DrawLine(Game.ReturnStackCopied(1), 1, "a")
                print(" ", end='')
            if i is 1:
                self.DrawLine(Game.ReturnStackCopied(1), 1, "b")
                print(" ", end='')
            if i is 2:
                self.DrawLine(Game.ReturnStackCopied(1), 1, "c")
                print(" ", end='')

        print()


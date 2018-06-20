from Stack import Stack
class HanoiGame:
    _firstStack = Stack()
    _secondStack = Stack()
    _thridStack = Stack()
   
    
    def __init__(self, numberOfDisks):
        if numberOfDisks == None:
            raise ValueError("The number of disks must be given")
        if numberOfDisks < 2 or numberOfDisks > 10:
            raise ValueError("The number of disks has to be between 2 and 10")
        self._initialize_Game_Field(numberOfDisks)

    def _initialize_Game_Field(self, numberOfDisks):
         for i in range(3,0,-1):
            self._firstStack.push(i)
        
    def turn(self, start, end):
        startStack = self._get_stack(start)
        endStack = self._get_stack(end)
        self._check_turn(start, end)
        endStack.push(startStack.pop())
    
    def _check_turn(self, start, end):
        if start is end:
           raise ValueError("The start stack could not be the end stack")

        startStack = self._get_stack(start)
        endStack = self._get_stack(end)

        if startStack.isEmpty == True:
            raise AssertionError("There is no Disk on the startStack")
        if endStack.isEmpty == False and startStack.Peek() > endStack.Peek():
            raise AssertionError("The Disk of the startStack is bigger than the Disk from the endstack")

       
    def _get_stack(self, input):
       if input is 1:
           return self._firstStack
       if input is 2:
           return self._secondStack
       if input is 3:
           return self._thridStack
       ValueError: "Invalid stack, has to be 1, 2 or 3"
        
        
            

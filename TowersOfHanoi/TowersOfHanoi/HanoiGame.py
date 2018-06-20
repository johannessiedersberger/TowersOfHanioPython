class HanoiGame:
    _firstStack = []
    _secondStack = []
    _thridStack = []
   
    
    def __init__(self, numberOfDisks):
        if numberOfDisks == None:
            raise ValueError("The number of disks must be given")
        if numberOfDisks < 2 or numberOfDisks > 10:
            raise ValueError("The number of disks has to be between 2 and 10")
        for i in range(3,-1,-1):
            self._firstStack
        
    def turn(self, start, end):
        startStack = self._get_stack(start)
        endStack = self._get_stack(end)
        self._check_turn(start, end)
        print(start + end)
    
    def _check_turn(self, start, end):
        if start is end:
           raise ValueError("The start stack could not be the end stack")

        startStack = self._get_stack(start)

    def _get_stack(self, input):
       if input is 1:
           return self._firstStack
       if input is 2:
           return self._secondStack
       if input is 3:
           return self._thridStack
       ValueError: "Invalid stack, has to be 1, 2 or 3"
        
        
            

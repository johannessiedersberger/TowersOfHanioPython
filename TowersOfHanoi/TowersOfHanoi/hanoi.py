from enum import Enum

class Stack(Enum):
    START = 0
    HELPER = 1
    DESTINATION =2

class Hanoi:
    """Play 'Towers of Hanoi' with a certain number of disks.
    
    Key arguments:
    num_disks -- Number of disks to play with (valid range is from 2 to 10)
    """
    
    def __init__(self, num_disks: int):
        """Creates the game board

        Key arguments:
        num_disks -- Number of disks to play with (valid range is from 2 to 10)

        >>> game = Hanoi(3)
        >>> game
        Hanoi(3)
        """
        if num_disks == None:
            raise TypeError
        if num_disks < 2 or num_disks > 10:
            raise ValueError('The number of disks has to be between 2 and 10, but was {}'.format(num_disks))

        self._stacks = {
            Stack.START: [val for val in range(num_disks, 0 , -1)],
            Stack.HELPER: [],
            Stack.DESTINATION: []
        }

    def __repr__(self):
        """Gets the object representation.
        >>> game = Hanoi(3)
        >>> game
        Hanoi(3)
        """
        return 'Hanoi({})'.format(self.num_disks)

    def __str__(self):
        """Prints the game board.
        >>> game = Hanoi(3)
        >>> print(game)
        {START: [3, 2, 1], HELPER: [], DESTINATION: []}
        """
        return '{{START: {}, HELPER: {}, DESTINATION: {}}}'.format(*(self._stacks[stack] for stack in Stack))
        
    def turn(self, start: Stack, end: Stack):
        """Moves a disk from the start stack to the end stack.
        
        >>> game = Hanoi(3)
        >>> game.turn(Stack.START, Stack.HELPER)
        >>> game[Stack.START]
        [3, 2]
        >>> game[Stack.HELPER]
        [1]
        >>> game.turn(Stack.START, Stack.HELPER)
        Traceback (most recent call last):
            ...
        ValueError: Disk from start stack is larger than disk on destination stack
        >>> game.turn(Stack.DESTINATION, Stack.HELPER)
        Traceback (most recent call last):
            ...
        ValueError: Start stack is empty
        """
        start = self._stacks[start]
        end = self._stacks[end]

        if len(start) == 0:
            raise ValueError('Start stack is empty')
        if len(end) > 0 and start[-1] > end[-1]:
            raise ValueError("Disk from start stack is larger than disk on destination stack")

        end.append(start.pop())
   
    def __getitem__(self, key: Stack):
        """Gets the stack defined by the key.
        >>> game = Hanoi(3)
        >>> game[Stack.START]
        [3, 2, 1]
        """
        return list(self._stacks[key])

    def __bool__(self):
        """Gets whether the game is still running.
        >>> game = Hanoi(3)
        >>> if game: print('RUNNING')
        RUNNING
        """
        return len(self._stacks[Stack.DESTINATION]) != self.num_disks

    @property
    def num_disks(self):
        """Gets the number of disks in the game.
        >>> game = Hanoi(3)
        >>> game.num_disks
        3
        """
        return sum([len(self._stacks[stack]) for stack in Stack], 0)


    
        
        

            

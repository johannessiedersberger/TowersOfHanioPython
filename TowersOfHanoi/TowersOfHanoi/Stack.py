class Stack:

     def __init__(self, arr=None):
         if arr is None:
             self.items = []
         else:
             self.items = arr

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)

     def copy(self):
         return Stack(self.items[:])

     def sort(self):
         return self.items.sort()

     def index(self, pos):
        return self.items[pos]

         

  

     
          

     
        


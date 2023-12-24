# Name: Yuhua Huang 
# 6 March 2023 
#this code defines a Stack class that can be used to implement a stack data structure in Python.
#got this implement from previous lab and class examples

class Stack:
    
    def __init__(self): #initializes the items attribute of the Stack object to an empty list.
        self.items = []

    def isEmpty(self): #checks if the items attribute of the Stack object is empty and returns True if it is and False otherwise.
        return self.items == []

    def push(self, item): #adds an item to the top of the items list of the Stack object.
        self.items.append(item)

    def pop(self): #removes and returns the item from the top of the items list of the Stack object.
        if len(self.items) == 0:
            return None
        return self.items.pop()
    
    def peek(self): #returns the item from the top of the items list of the Stack object without removing it.
        if len(self.items) == 0:
            return None
        return self.items[len(self.items)-1]

    def size(self): # returns the number of items in the items list of the Stack object.
         return len(self.items)

# a driver program for class Stack

if __name__ == '__main__':
    
    data_in = ['hello', 'how', 'are', 'you']
    s = Stack()
    for i in data_in:
        s.push(i)
           
    assert s.size() == len(data_in)
    assert s.peek() == data_in[-1]

    data_out = []
    while not s.isEmpty():
        data_out.append(s.pop())

    assert data_out == data_in[::-1]
    assert s.size() == 0
    assert s.peek() == None

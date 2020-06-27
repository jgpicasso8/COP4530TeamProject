# Authors: Andres Greene
#         Raquel Garcia
#         Laureano Griffin
#         Josue Gonzalez-Picasso

class Dynamic_queue:

    # Constructor
    def __init__(self, value=10):
        # Initializes attributes
        self.elements = []
        self.iHead = 0
        self.iTail = 0
        self.entryCount = 0
        # Sets capacity equal to 1 if the value is equal to zero or lower
        if value <= 0:
            self.currCapacity, self.initialCapacity = 1, 1
        else:
            self.currCapacity, self.initialCapacity = value, value

    # Destructor
    def __del__(self):
        return

    # Copy Constructor - creates a new instance of queue ***
    def __copy__(self):
        copy = Dynamic_queue(self.currCapacity)
        for x in self.elements:
            copy.elements[x] = self.elements[x]
        return copy

    # Accessors - access the queue, but doesn't modify it
    # Returns the object at the head of the queue
    def head(self):
        return

    # Returns the number of objects currently stored in the queue
    def size(self):
        return len(self.elements)

    # Returns true if the queue is empty. Returns false otherwise
    def empty(self):
        return

    # Returns the current capacity of the queue.
    def capacity(self):
        return self.currCapacity

    # Mutators - Changes values in the queue
    # will swap all the member variables of this queue with those of the argument
    def swap(self):
        return

    # Swaps member variables with with the copy on the right side of the operator ***
    def __equal__(self, copy):
        return copy

    # Insert the argument at the end of the queue. If the array is full before the argument is placed,
    # the array is doubled first.
    def enqueue(self, value):
        return

    # Removes the object at the front of the queue. If, after the object is removed, the array is ***
    # 1/4 full, and its greater than the initial capacity, the capacity is halved.
    def dequeue(self, value):
        return

    # Empties the queue. The array is resized to the initial capacity
    def clear(self):
        return

from Lab8 import ListSimple

class Queue:
    def __init__(self, data = None):
        self.__data = ListSimple()

    def size(self):
        return self.__data.size()
    
    def isEmpty(self):
        return self.__data.isEmpty()
    
    def enqueue(self,o):
        return self.__data.addLast(o)

    def dequeue(self):
        return self.__data.removeFirst()
    
    def first(self):
        return self.__data.first()

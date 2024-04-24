from NodeSimple import NodeSimple

class ListSimple:
    def __init__ (self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def size(self):
        return self.size
    
    def isEmpty(self):
        return self.size == 0
    
    def setSize(self, size):
        self.size = size
    
    def First(self):
        return self.head
    
    def Last(self):
        return self.tail
    
    def addFirst(self, data):
        newNode = NodeSimple(data)
        if self.isEmpty():
            self.head = newNode
            self.tail = newNode
        else:
            newNode.setNext(self.head)
            self.head = newNode
        self.size += 1

    def addLast(self, data):
        newNode = NodeSimple(data)
        if self.isEmpty():
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.setNext(newNode)
            self.tail = newNode
        self.size += 1
    
    def removeFirst(self):
        if self.isEmpty():
            raise Exception("List is empty")
        nodoDelete = self.head
        self.head = nodoDelete.getNext()
        nodoDelete.setNext(None)
        self.size -= 1
        return nodoDelete.getData()
    
    def removeLast(self):
        if self.size == 1:
            return self.removeFirst()
        else:
            nodoDelete = self.tail
            nodoBefore = self.head
            while nodoBefore.getNext() != self.tail:
                nodoBefore = nodoBefore.getNext()
            nodoBefore.setNext(None)
            self.tail = nodoBefore
            self.size -= 1
            return nodoDelete.getData()
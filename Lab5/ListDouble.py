from NodeDouble import NodeDouble

class ListDouble:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def __str__(self):
        if self.isEmpty():
            return "List is empty"
        else:
            node = self.head
            result = ""
            while node != None:
                result += str(node.getData()) + " "
                node = node.getNext()
            return result

    def size(self):
        return self.size
    
    def isEmpty(self):
        return self.size == 0
    
    def setSize(self, size):
        self.size = size

    def first(self):
        return self.head
    
    def last(self):
        return self.tail
    
    def addFirst(self, data):
        newNode = NodeDouble(data)
        if self.isEmpty():
            self.head = newNode
            self.tail = newNode
        else:
            newNode.setNext(self.head)
            self.head.setPrev(newNode)
            self.head = newNode
        self.size += 1
        self.setSize(self.size)
    
    def addLast(self, data):
        newNode = NodeDouble(data)
        if self.isEmpty():
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.setNext(newNode)
            newNode.setPrev(self.tail)
            self.tail = newNode
        self.size += 1
        self.setSize(self.size)
    
    def removeFirst(self):
        if self.isEmpty():
            raise Exception("List is empty")
        nodeDelete = self.head
        self.head = nodeDelete.getNext()
        nodeDelete.setNext(None)
        self.head.setPrev(None)
        self.size -= 1
        self.setSize(self.size)
        return nodeDelete.getData()
    
    def removeLast(self):
        if self.isEmpty():
            raise Exception("List is empty")
        nodeDelete = self.tail
        self.tail = nodeDelete.getPrev()
        self.tail.setNext(None)
        nodeDelete.setPrev(None)
        self.size -= 1
        self.setSize(self.size)
        return nodeDelete.getData()
    
    def remove(self, node):
        if node == self.head:
            return self.removeFirst()
        elif node == self.tail:
            return self.removeLast()
        else:
            nodeDelete = node
            nodeAfter = node.getPrev()
            nodeBefore = node.getNext()
            nodeAfter.setNext(nodeBefore)
            nodeBefore.setPrev(nodeAfter)
            nodeDelete.setNext(None)
            nodeDelete.setPrev(None)
            self.size -= 1
            self.setSize(self.size)
            return nodeDelete.getData()
        
    def delete(self, data):
        if self.isEmpty():
            raise Exception("List is empty")
        node = self.head
        while node != None:
            if node.getData() == data:
                return self.remove(node)
            node = node.getNext()
        raise Exception("Data not found")

    def addBefore(self, node, data):
        if node == self.head:
            self.addFirst(data)
        else:
            newNode = NodeDouble(data)
            nodeBefore = node.getPrev()
            newNode.setPrev(nodeBefore)
            newNode.setNext(node)
            nodeBefore.setNext(newNode)
            node.setPrev(newNode)
            self.size += 1
            self.setSize(self.size)

    def addAfter(self, node, data):
        if node == self.tail:
            self.addLast(data)
        else:
            newNode = NodeDouble(data)
            nodeAfter = node.getNext()
            newNode.setPrev(node)
            newNode.setNext(nodeAfter)
            node.setNext(newNode)
            nodeAfter.setPrev(newNode)
            self.size += 1
            self.setSize(self.size) 
        
from NodeDouble import NodeDouble

class ListDouble:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

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
    
    def addLast(self, data):
        newNode = NodeDouble(data)
        if self.isEmpty():
            self.head = newNode
            self.tail = newNode
        else:
            newNode.setPrev(self.tail)
            self.tail.setNext(newNode)
            self.tail = newNode
        self.size += 1
    
    def removeFirst(self):
        if self.isEmpty():
            raise Exception("List is empty")
        nodeDelete = self.head
        self.head = nodeDelete.getNext()
        nodeDelete.setNext(None)
        self.head.setPrev(None)
        self.size -= 1
        return nodeDelete.getData()
    
    def removeLast(self):
        if self.isEmpty():
            raise Exception("List is empty")
        nodeDelete = self.tail
        self.tail = nodeDelete.getPrev()
        self.tail.setNext(None)
        nodeDelete.setPrev(None)
        self.size -= 1
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
            return nodeDelete.getData()

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
        
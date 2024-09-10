class Node:
    def __init__(self, data):
        self.data  = data
        self.left  = Node
        self.right = Node

    def __str__(self):
        return str(self.data)
    
    def getData(self):
        return self.data
    
    def setData(self, data):
        self.data = data

    def getRight(self):
        return self.right
    
    def setRight(self, n):
        self.right = n
    
    def getLeft(self):
        return self.left
    
    def setLeft(self, n):
        self.left = n
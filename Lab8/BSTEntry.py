from BinaryTree import BinaryTree
from Node import Node

class BSTEntry:

    def __init__(self, e = object, k = int):
        self.data = e
        self.k = k

    def getData(self):
        return self.data
    
    def setData(self,d = object):
        self.data = d
    
    def getKey(self):
        return self.k
    
    def setKey(self, k = int):
        self.k = k

    
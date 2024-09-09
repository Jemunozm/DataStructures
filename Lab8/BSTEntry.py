from BinaryTree import BinaryTree
from NodeDouble import NodeDouble

class BSTEntry:

    def __init__(self, e = object, k = int):
        self._data = e
        self._k = k

    def getData(self):
        return self._data
    
    def setData(self,d=object):
        self._data = d
    
    def getKey(self):
        return self._k
    
    def setKey(self, k = int):
        self._k = k

    
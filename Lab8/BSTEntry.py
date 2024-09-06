from Lab8 import BinaryTree
from Lab8 import NodeDouble

class BSTEntry(BinaryTree):

    def __init__(self, e = object, k = int):
        self._data = e
        self._k = k

    def getData(self):
        return self.data
    
    def setData(self,d=object):
        self.data = d
    
    def getKey(self):
        return self.k
    
    def setKey(self, k = int):
        self.k = k

    def searchTree(self, k = int, v = NodeDouble):
        u = BSTEntry
        u = v.getData()
        if k==u.getKey():
            return v
        elif k < u.getKey():
            return self.searchTree(k,v.getLeft())
        else:
            return self.datasearchTree(k,v.getRight())


    def find(self, k = int):
        return searchTree(self, k, root)
    
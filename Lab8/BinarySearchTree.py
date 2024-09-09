from BinaryTree import BinaryTree
from BSTEntry import BSTEntry
from NodeDouble import NodeDouble

def BinarySearchTree(BinaryTree):

     
    def searchTree(k = int, v = NodeDouble):
        u = BSTEntry()
        u = v.getData()
        if k==u.getKey():
            return v
        elif k < u.getKey():
            return searchTree(k,v.getLeft())
        else:
            return searchTree(k,v.getRight())

    def find(k = int):
        return searchTree(k, root)
    
    def addEntry(v = NodeDouble, o = BSTEntry):
        temp = BSTEntry()
        temp = v.getData()
        nD   = NodeDouble(o)
        if o.getKey()<temp.getKey():
            if hasLeft(v):
                addEntry(Left(v), o)
            else:
                v.setLeft(nD)
        else:
            if hasRight(v):
                addEntry(right(v), o)
            else: 
                v.setRight(nD)
    
    def insert(e = object, k = int):
        O = BSTEntry(e,k)
        if isEmpty():
            super.addRoot(O)
        else:
            addEntry(root,O)
    
    def maxNode(temp = NodeDouble):
        if hasRight(temp):
            return maxNode(right(temp))
        else:
            return temp
        
    def predecesor(v = NodeDouble):
        temp = NodeDouble()
        temp = temp.getLeft()
        return maxNode(temp)
    
    def Remove(k = int):
        v = NodeDouble()
        v = find(k)
        temp = v.getData()
        if hasLeft(v) and hasRight(v):
            w = NodeDouble()
            w = predecesor(v)
            v.setData(w.getData())
            super.remove(w)
        else:
            super.remove(v)
        return temp
from BinaryTree import BinaryTree
from BSTEntry import BSTEntry
from Node import Node

def BinarySearchTree(BinaryTree = BinaryTree):

    #def __init__(self):
        #super().__init__()

    
     
    def searchTree(k = int, v = Node):
        u = BSTEntry(v,v.getData())
        #u = v.getData()
        if k == u.getKey():
            return v
        elif k < u.getKey():
            return searchTree(k,v.getLeft())
        else:
            return searchTree(k,v.getRight())

    def find(k = int):
        return searchTree(k, BinaryTree.root)
    
    def addEntry(v = Node, o = BSTEntry):
        temp = BSTEntry(v,v.getData())
        #temp = v.getData()
        nD   = Node(o)
        if o.getKey() < temp.getKey():
            if BinaryTree.hasLeft(v):
                addEntry(BinaryTree.left(v), o)
            else:
                v.setLeft(nD)
        else:
            if BinaryTree.hasRight(v):
                addEntry(BinaryTree.right(v), o)
            else: 
                v.setRight(nD)
    
    def insert(e = object, k = int):
        O = BSTEntry(e,k)
        if BinaryTree.isEmpty():
            BinaryTree.addRoot(O)
        else:
            addEntry(BinaryTree.root,O)
    
    def maxNode(temp = Node):
        if BinaryTree.hasRight(temp):
            return maxNode(BinaryTree.right(temp))
        else:
            return temp
        
    def predecesor(v = Node):
        temp = Node()
        temp = temp.getLeft()
        return maxNode(temp)
    
    def Remove(k = int):
        v = Node()
        v = find(k)
        temp = v.getData()
        if BinaryTree.hasLeft(v) and BinaryTree.hasRight(v):
            w = Node()
            w = predecesor(v)
            v.setData(w.getData())
            BinaryTree.remove(w)
        else:
            BinaryTree.remove(v)
        return temp
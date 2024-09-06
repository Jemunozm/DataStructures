from Lab8 import NodeDouble
from Lab8 import Queue

class BinaryTree:
    def __init__(self):
       self.root = None
       self.size = 0

    def root(self):
        return self.root
    
    def size(self):
        return self.size

    def isEmpty(self):
        return self.size == 0
    
    def isRoot(self, node):
        return node == self.root
    
    def left(self, node):
        return node.getLeft()
    
    def right(self, node):
        return node.getRight()
    
    def hasLeft(self, node):
        return node.getLeft()!=None

    def hasRight(self, node):
        return node.getRight()!=None
 
    def isInternal(self, node):
        return self.hasLeft(node) or self.hasRight(node)
    
    def Parent(self, node):
        if self.isRoot(node):
            return None
        else:
            Q = Queue()
            Q.enqueue(self.root)
            temp = NodeDouble(self.root)
        while (not Q.isEmpty() & self.left(Q.first()) != node & self.right(Q.first()) != node):
            temp = Q.dequeue()
            if self.hasLeft(temp):
                Q.enqueue(self.left(temp))
            if self.hasRight(temp):
                Q.enqueue(self.right(temp))
            return temp
    
    def depth(self, node):
        if self.isRoot(node):
            return 0
        else:
            return 1 + self.depth(self.parent(node))
    
    def height(self, node):
        if not (self.isInternal(node)):
            return 0
        else: 
            h = 0
            h = max(self.height(self.left(node)),self.height(self.right(node)))
            return 1 + h 
        
    def addRoot(self,e):
        self.root = NodeDouble(e)
        self.size = 1
    
    def insertLeft(self, v=NodeDouble, e=object):
        nodeLeft = NodeDouble(e)
        v.setLeft(nodeLeft)
        self.size += 1

    def insertRight(self, v=NodeDouble, e=object):
        nodeRight = NodeDouble(e)
        v.setRight(nodeRight)
        self.size += 1

    def remove(self, v=NodeDouble):
        p = self.Parent(v)
        # v tiene al menos un hijo - caso 1
        if self.hasLeft(v) or self.hasRight(v):
            if self.hasLeft(v):
                child = self.left(v)
            else:
                child = self.right(v)
            # Se conecta el hijo de v al padre
            if self.left(p) == v:
                p.setLeft(child)
            else:
                p.setNext(child)
            #se conecta al nodo v
            v.setLeft(None)
            v.setRight(None)
        #si v no tiene hijos - caso 2
        else:
            if self.left(p)==v:
                p.setLeft(None)
            else:
                p.setRight(None)
        self.size -= 1

    def visit(self,v=NodeDouble, caso=int):
        if caso==1:
            file = open("archivo1", "w")
            file.write(v.getData())
            file.close()
        elif caso ==2:
            acumulador = 0
            acumulador += v.getData()
        else:
            print(v.getData())

    def Preorder(self, v=NodeDouble):
        self.visit(v)
        if self.hasLeft(v):
            self.Preorder(self,self.left(v))
        if self.hasRight(v):
            self.Preorder(self,self.right(v))

    def Inorder(self, v=NodeDouble):
        if self.hasLeft(v):
            self.Inorder(self,self.left(v))
        self.visit(v)
        if self.hasRight(v):
            self.Ineorder(self,self.right(v))
    
    def Posorder(self, v=NodeDouble):
        if self.hasLeft(v):
            self.Posorder(self, self.left(v))
        if self.right(v):
            self.Posorder(self, self.right(v))
        self.visit(v)
    
    def minB(self,v=NodeDouble):
        if self.hasLeft(v):
            return min(self, self.hasLeft(v))
        else:
            return v.getData()
    def maxB(self,v=NodeDouble):
        if self.hasRight(v):
            return min(self, self.hasRight(v))
        else:
            return v.getData()
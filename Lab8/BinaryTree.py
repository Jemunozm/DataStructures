from Node import Node
from Queue import Queue

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
    
    def isRoot(self, node = Node):
        return node == self.root
    
    def left(self, node = Node):
        return node.getLeft()
    
    def right(self, node = Node):
        return node.getRight()
    
    def hasLeft(self, node = Node):
        return node.getLeft()!=None

    def hasRight(self, node = Node):
        return node.getRight()!=None
 
    def isInternal(self, node = Node):
        return self.hasLeft(node) or self.hasRight(node)
    
    def Parent(self, node = Node):
        if self.isRoot(node):
            return None
        else:
            Q = Queue()
            Q.enqueue(self.root)
            temp = Node(self.root)
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
            return 1 + self.depth(self.Parent(node))
    
    def height(self, node):
        if not (self.isInternal(node)):
            return 0
        else: 
            h = 0
            h = max(self.height(self.left(node)),self.height(self.right(node)))
            return 1 + h 
        
    def addRoot(self,e):
        self.root = Node(e)
        self.size = 1
    
    def insertLeft(self, v=Node, e=object):
        nodeLeft = Node(e)
        v.setLeft(nodeLeft)
        self.size += 1

    def insertRight(self, v=Node, e=object):
        nodeRight = Node(e)
        v.setRight(nodeRight)
        self.size += 1

    def remove(self, v = Node):
        p = Node(self.Parent(v))
        #p = self.Parent(v)
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

    def visit(self,v=Node, caso=int):
        if caso==1:
            file = open("archivo1", "w")
            file.write(v.getData())
            file.close()
        elif caso ==2:
            acumulador = 0
            acumulador += v.getData()
        else:
            print(v.getData())

    def preorder(self, v=Node):
        self.visit(v)
        if self.hasLeft(v):
            self.preorder(self,self.left(v))
        if self.hasRight(v):
            self.preorder(self,self.right(v))

    def inorder(self, v=Node):
        if self.hasLeft(v):
            self.inorder(self,self.left(v))
        self.visit(v)
        if self.hasRight(v):
            self.inorder(self,self.right(v))
    
    def posorder(self, v=Node):
        if self.hasLeft(v):
            self.posorder(self, self.left(v))
        if self.right(v):
            self.posorder(self, self.right(v))
        self.visit(v)
    
    def minB(self,v=Node):
        if self.hasLeft(v):
            return min(self, self.hasLeft(v))
        else:
            return v.getData()
    def maxB(self,v=Node):
        if self.hasRight(v):
            return min(self, self.hasRight(v))
        else:
            return v.getData()
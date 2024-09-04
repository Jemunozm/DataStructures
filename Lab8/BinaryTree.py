from Lab8 import NodeDouble

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
            Q = newQueue()
            Q.enqueue(root)
            temp = NodeDouble(root)
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
            h = max(self.height(left(node)),self.height(right(node)))
            return 1 + h
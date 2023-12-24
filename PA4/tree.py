
# Name: Yuhua Huang
# 6 March 2023
# Creates a BinaryTree object (each parents has at least 2 children) & ExpressionTree
# which is a pretty much a BinaryTree that orders based on priority of calculations (PEMDAS)

from stack import Stack

class BinaryTree:  #instance variable key that holds the value of the node, and two instance variables leftChild and rightChild that hold references to the left and right children of the node. 
    def __init__(self,rootObj=None):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self,newNode): #used to insert a new node as the left child of the current node. If the child node already exists, it is pushed down the tree and the new node is inserted in its place.
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self,newNode): #used to insert a new node as the right child of the current node. If the child node already exists, it is pushed down the tree and the new node is inserted in its place.
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t

    def getRightChild(self): #methods return the right child of the current node
        return self.rightChild

    def getLeftChild(self): #methods return the left child of the current node
        return self.leftChild

    def setRootVal(self,obj): #sets the value of the current node.
        self.key = obj

    def getRootVal(self): #eturns the value of the current node.
        return self.key

    def __str__(self): #returns a string representation of the binary tree in a nested format, with each node represented by its value, and its left and right children recursively nested within parentheses.
        s = f"{self.key}"
        s += '('
        if self.leftChild != None:
            s += str(self.leftChild)
        s += ')('
        if self.rightChild != None:
            s += str(self.rightChild)
        s += ')'
        return s

class ExpTree(BinaryTree):

    def make_tree(postfix): #takes a postfix expression as input and uses a stack to build an expression tree by iterating through the postfix expression. It returns the root node of the resulting expression tree.
        s = Stack()
        for i in range(len(postfix)):
            if (postfix[i] not in '()^*/+-'):
                s.push(ExpTree(postfix[i]))
            else:
                temp = ExpTree(postfix[i])
                temp.rightChild = s.pop()
                temp.leftChild = s.pop()
                s.push(temp)
        return s.peek()

    def preorder(tree): #got this implentment from PA4 lecture slide notes 
        s = ''
        if (tree != None):
            s += tree.getRootVal()
            if tree.leftChild != None:
                s += ExpTree.preorder(tree.getLeftChild())
            if tree.rightChild != None:
                s += ExpTree.preorder(tree.getRightChild())
        return s

    def inorder(tree): #perform a traversal of the expression tree in inorder. They return a string representation of the corresponding traversal order.
        s = ''
        if (tree != None):
            if tree.leftChild != None:
                s += '('
                s += ExpTree.inorder(tree.getLeftChild())
            s += str(tree.getRootVal())
            if tree.rightChild != None:
                s += ExpTree.inorder(tree.getRightChild())
                s += ')'
        return s
      
    def postorder(tree): #perform a traversal of the expression tree in postorder. They return a string representation of the corresponding traversal order.
        s = ''
        if tree:
            if tree.leftChild != None:
                s += ExpTree.postorder(tree.getLeftChild())
            if tree.rightChild != None:
                s += ExpTree.postorder(tree.getRightChild())
            s += str(tree.getRootVal())
        return s

    def evaluate(tree): #takes an expression tree as input and recursively evaluates the expression using a dictionary of lambda functions for each operator. It returns the result of the expression evaluation.
        op = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '/': lambda x, y: x / y,
            '^': lambda x, y: x ** y
        }
        if tree.getLeftChild() and tree.getRightChild():
            fn = op[tree.getRootVal()]
            return fn(ExpTree.evaluate(tree.getLeftChild()), ExpTree.evaluate(tree.getRightChild()))
        else:
            return float(tree.getRootVal())
            
    def __str__(self): #returns the inorder traversal of the expression tree as a string, which represents the original infix expression.
        return ExpTree.inorder(self)
   
# a driver for testing BinaryTree and ExpTree
if __name__ == '__main__':

    # test a BinaryTree
    
    r = BinaryTree('a')
    assert r.getRootVal() == 'a'
    assert r.getLeftChild()== None
    assert r.getRightChild()== None
    assert str(r) == 'a()()'

    
    r.insertLeft('b')
    assert r.getLeftChild().getRootVal() == 'b'
    assert str(r) == 'a(b()())()'
    
    r.insertRight('c')
    assert r.getRightChild().getRootVal() == 'c'
    assert str(r) == 'a(b()())(c()())'
    
    r.getLeftChild().insertLeft('d')
    r.getLeftChild().insertRight('e')
    r.getRightChild().insertLeft('f')
    assert str(r) == 'a(b(d()())(e()()))(c(f()())())'

    assert str(r.getRightChild()) == 'c(f()())()'
    assert r.getRightChild().getLeftChild().getRootVal() == 'f'

    
    # test an ExpTree
    
    postfix = '5 2 3 * +'.split()
    tree = ExpTree.make_tree(postfix)
    
    assert str(tree) == '(5+(2*3))'
    assert ExpTree.inorder(tree) == '(5+(2*3))'
    assert ExpTree.postorder(tree) == '523*+'
    assert ExpTree.preorder(tree) == '+5*23'
    assert ExpTree.evaluate(tree) == 11.0

    postfix = '5 2 + 3 *'.split()
    tree = ExpTree.make_tree(postfix)
    
    assert str(tree) == '((5+2)*3)'
    assert ExpTree.inorder(tree) == '((5+2)*3)'
    assert ExpTree.postorder(tree) == '52+3*'
    assert ExpTree.preorder(tree) == '*+523'
    assert ExpTree.evaluate(tree) == 21.0
    
    
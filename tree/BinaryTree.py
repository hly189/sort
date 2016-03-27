from Stack import Stack


class BinaryTree:

    def __init__(self,x):
      self.left = None
      self.right = None
      self.root = x

    def getLeftChild(self):
        return self.left
    def getRightChild(self):
        return self.right
    def setNodeValue(self,value):
        self.root = value
    def getNodeValue(self):
        return self.root

    def insertRight(self,newNode):
        if self.right == None:
            self.right = BinaryTree(newNode)
        else:
            tree = BinaryTree(newNode)
            tree.right = self.right
            self.right = tree
        
    def insertLeft(self,newNode):
        if self.left == None:
            self.left = BinaryTree(newNode)
        else:
            tree = BinaryTree(newNode)
            self.left = tree
            tree.left = self.left


class Solution:
    # @param num, a list of integers
    # @return a tree node
    def insertArray(self, num):
        return self.insertArray_helper(num, 0, len(num))
    
    def insertArray_helper(self, num, start, end):
        if start == end:
            return None
        mid = start + (end - start) / 2
        node = BinaryTree(num[mid])
        node.left = self.insertArray_helper(num, start, mid)
        node.right = self.insertArray_helper(num, mid + 1, end)
        return node

    def convert(self,value): 
    	if len(value) == 0: return None

    	i = 1
    	node = BinaryTree(value[0])

    	while i < len(value): 
    		if value[i] == '?':
    			node.insertLeft(value[i+1])
    		elif value[i] == ':': 
    			node.insertRight(value[i+1])
    		i = i +1 
    	
    	return node 



            
def printTree(root):
    print_helper(root, "")

def print_helper(root, indent):
    if root is not None:
        print_helper(root.right, indent + " ")
        print (indent + str(root.root))
        print_helper(root.left, indent + " ")

def print_tree(tree):
        if tree != None:
            printTree(tree.getLeftChild())
            print(tree.getNodeValue())
            printTree(tree.getRightChild())

s = [1,2,3,4]
a = 'a?b:c:d'

binarytree = Solution().insertArray(s)
tenary1 = Solution().convert(a)

def testTree():
    myTree = BinaryTree("Maud")
    myTree.insertLeft("Bob")
    myTree.insertRight("Tony")
    myTree.insertRight("Steven")
    printTree(myTree)
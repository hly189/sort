class Node: 
	def __init__(self, val,key):
		self.key = key 
		self.value = val
		self.left = None 
		self.right = None 

	def get_left(self):
		return self.left

	def get_right(self): 
		return self.right

	def set_right_equal(self,data): 
		self.right = data

	def set_left_equal(self,data): 
		self.left = data

	def count(self): 
		count = 0
		if self.left is not None: 
			count = count + 1
		if self.right is not None: 
			count =  count + 1

	def find(self,key): 
		if self.item == key: 
			return False
		else: 
			if self.left is not None: 
				return self.left.find(key)
			else: 
				return self.right.find(key)


class BinaryTree(object):	
	def __init__(self,item): 
		self.item = item 
		self.root = None
		self.size = 0

	def get_size(self):
		return self.size  

	def get_item(self): 
		return self.item

	def set_item_equal(self, data): 
		self.item = data 

	def insert_right(self, key): 
		current = self.root 
		if self.right is None: 
			self.right = BinaryTree(key)
		else: 
			tree = BinaryTree(key)
			tree.right = self.right
			self.right = tree
		self.size = self.size + 1

	def insert_left(self, key): 
		if self.left is None: 
			self.left = BinaryTree(key)
		else: 
			tree = BinaryTree(key)
			tree.left = self.left
			self.left= tree
		self.size = self.size + 1

	def find(self,key): 
		if self.root is not None: 
			return self.root.find(key)
		else: 
			return False 

def printTree(tree): 
	if tree != None:  
		printTree(tree.get_left_child())
		print(tree.get_item())
		printTree(tree.get_right_child())



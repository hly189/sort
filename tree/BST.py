class BSTreeNode: 
	def __init__(self, value): 
		self.value = value 
		self.left = None 
		self.right = None

	def insert(self,key): 
		if self.value == key: 
			print ("the node already exists")
			return False 
		elif self.value > key: 
			if self.left is not None: 
				return self.left.insert(key)
			else: 
				self.left = BSTreeNode(key)
				return True
		else: 
			if self.right is not None: 
				return self.right.insert(key)
			else: 
				self.right = BSTreeNode(key)
				return False
	
	def delete(self, node, k):
		if node == None: 
			return None
		elif node.value == k: 
			if node.left is None and node.right is None: 
				return None
			elif node.left is None: 
				return node.right
			elif node.right is None: 
				return node.left 
			else: 
				node.value = get_min(node.right)
				node.right.delete(node.right,node.value)
		elif k < node.value: 
			node.left.delete(node.left,k)
		else: 
			node.right.delete(node.right,k)
		return node


	def pre_order(self): 
		if self: 
			print (str(self.value))
			if self.left: 
				self.left.pre_order()
			if self.right:
				self.right.pre_order()

	def in_order(self): 
		if self: 
			if self.left: 
				self.left.in_order()
			print(str(self.value))
			if self.right: 
				self.right.in_order()

	def post_order(self):
		if self: 
			if self.left: 
				self.left.post_order()
			if self.right: 
				self.right.post_order()
			print(str(self.value))
				


class BSTree: 
	def __init__(self): 
		self.root = None 

	def delete(self,key): 
		self.root.delete(self.root,key)

	def insert(self,data): 
		if self.root: 
			self.root.insert(data)
		else: 
			self.root = BSTreeNode(data)
			return True 

	def search_iter(self,key): 
		current = self.root

		while current is not None: 
			if current.value ==key: 
				return current
			elif key < current.value: 
				current = current.left 
			else: 
				current = current.right
		return None

	def find_min(self,node):
		current_node = node
		while current_node.left: 
			current_node = current_node.left
		return current_node

	def pre_order(self): 
		self.root.pre_order() 

	def in_order(self): 
		self.root.in_order()

	def post_order(self): 
		self.root.post_order()


def search_recursive(node,key): 
	if node is None or node.value == key: 
		return node 
	elif key < node.value: 	
		return search(node.left, key)
	else: 
		return search(node.right, key)
	return None 

def print_tree(root):
    print_helper(root, "")

def get_min(node): 
	current_node = node
	while current_node.left: 
		current_node = current_node.left
	return current_node

def print_helper(root, indent):
    if root is not None:
        print_helper(root.right, indent + "   ")
        print (indent + str(root.value))
        print_helper(root.left, indent + "   ")

bst = BSTree()
bst.insert(5)
bst.insert(11)
bst.insert(15)
bst.insert(3)
bst.insert(4)
bst.insert(6)
bst.insert(12)



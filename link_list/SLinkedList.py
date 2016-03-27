class SListNode(object):
	"""Node for Singly Linked List """
	def __init__(self, item, next = None):
		self.item = item 
		self.next = next

	def get_next(self): 
		return self.next

	def set_next_equal(self, n): 
		self.next = n
		return self.next 

	def get_item(self): 
		return self.item 

	def set_item_equal(self, d): 
		self.item = d
		return self.item 


class SList(object):
	"""Singly Linked List """
	def __init__(self, head = None):
		self.head = head
		self.size = 0

	def get_length(self): 
		return self.size

	def show(self): 
		current = self.head

		while current is not None: 
			print(current.item)
			current = current.get_next()
	
	def insertFont(self, d): 
		new_head = SListNode(d, self.head)
		self.head = new_head
		self.size = self.size + 1

	def insertEnd(self,d): 
		if self.head is None: 
			new_node = SListNode(d,None)
		else: 
			new_node = self.head 
			while new_node.next is not None: 
				new_node = new_node.get_next()
			new_node.next = SListNode(d,None)
			self.size = self.size + 1

	def find(self, position): 
		if position < 1 or self.head is None: 
			return None
		else: 
			current = self.head
			while position > 1: 
				current = current.get_next()
				if current is None: 
					return None 
				position = position -1 
			return current.get_item()

	def remove(self, key): 
		current = self.head
		previous = None

		while current is not None: 
			if current.get_item() == key: 
				if previous is not None: 
					previous.set_next_equal(current.get_next())
				else: 
					self.head = current.get_next()
			self.size = self.size - 1
			previous = current
			current = current.get_next()

	def remove_duplicate(self): 
		current = self.head

		while current is not None: 
			before_check = current
			check = current.next 

			while check is not None: 
				if check.item == current.item: 
					before_check.next = check.next
					check = check.next 
				else: 
					before_check = check 
					check = check.next

			current = current.next 

	def reverse_iter(self): 
		current = self.head
		previous = None
		next = None

		while current is not None:
			next = current.get_next()
			current.next = previous
			previous = current
			current = next
		self.head = previous 

	def merge_list(self, other):
		if self.head is None: 
			self.head = other.head
		else: 
			current = self.head
			while current.next is not None: 
				current = current.next
			current.next = other.head

	def to_string(self): 
		values = []
		current = self.head
		while current is not None: 
			values.append(str(current.item))	
			current = current.next
		return ','.join(values)


s = SList()
s.insertFont(1)
s.insertEnd(2)
s.insertEnd(2)
s.insertEnd(3)
s.insertEnd(4)

a = SList()
a.insertFont(5)
a.insertEnd(6)
a.insertEnd(7)
a.insertEnd(8)

		
class DListNode(object): 
    
    def __init__(self, item, previous = None, next = None): 
        self.item = item 
        self.previous = previous
        self.next = next 

    def get_item(self): 
        return self.item
    
    def set_item_equal(self,data):
        self.item = data
    
    def get_next(self): 
        return self.next 

    def set_next_equal(self,data): 
        self.next = data

    def get_previous(self): 
        return self.previous 

    def set_previous_equal(self,data): 
        self.previous = data

class DList(object):
    """docstring for DList"""
    def __init__(self, head = None):
        self.head = head 
        self.size = 0

    def get_length(self): 
        return self.size 

    def show(self): 
        current_node = self.head
        while current_node is not None: 
            print current_node.previous.item if hasattr(current_node.previous, "data") else None,
            print current_node.item 
            print current_node.next.item if hasattr(current_node.next, "data") else None
            current_node = current_node.next

    def insertEnd(self,data): 
        node = DListNode(data, self.head)

        if self.head :
            self.head.set_previous_equal(node)
        self.head = node
        self.size +=1

    def insertFont(self,data): 
        head = DListNode(None, None, self.head)
        node = DListNode(data, head, head.next)
        if self.size == 0:
            head.next = node
            head.previous = node 
        else: 
            head.next.previous = node
            head.next = node 
        self.size = self.size + 1

    def remove(self,key): 
        current = self.head
        while current is not None: 
            if current.get_item() == key: 
                if current.previous is not None: 
                    current.previous.next = current.next 
                    current.next.previous = current.previous
                else: 
                    self.head = current.next
                    current.next.previous = None
            current = current.next 
            self.size = self.size - 1

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


s = DList()
s.insertFont(2)
s.insertEnd(3)
s.insertEnd(4)
s.insertEnd(5)

        
        

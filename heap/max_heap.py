class MaxHeap: 
    def __init__(self,item = []): 
        super().__init__()
        self.heap = [0]
        for i in range(len(item)): 
            self.heap.append(item[i])
            self._floatUp(len(self.heap)-1)

    def push(self,data): 
        self.heap.append(data)
        self._floatUp(len(self.heap)-1)
        
    def peek(self): 
        if self.heap[1]: 
            return self.heap[1]
        else: 
            return False 

    def pop(self):
        if len(self.heap) > 2:
            self._swap(1, len(self.heap) - 1)
            max = self.heap.pop()
            self._bubble_down(1)
        elif len(self.heap) == 2:
            max = self.heap.pop()
        else: 
            max = False
        return max

    def _floatUp(self,i):
        parrent = i //2
        if i <= 1: 
            return 
        elif self.heap[parrent] < self.heap[i]: 
            self._swap(parrent,i)
            self._floatUp(parrent)

    def _bubble_down(self, index): 
        left = index * 2
        right = index * 2+ 1
        largest = index

        if len(self.heap) > left and self.heap[largest] < self.heap[left]: 
            largest = left

        if len(self.heap) > right and self.heap[largest] < self.heap[right]: 
            largest = right

        if largest != index: 
            self._swap(index ,largest)
            self._bubble_down(largest)
    
    def _swap(self,x,y):
        temp = self.heap[x]
        self.heap[x] = self.heap[y]
        self.heap[y] = temp
            
m = MaxHeap([4,3,1,5])

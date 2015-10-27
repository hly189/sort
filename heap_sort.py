from swap import swap

def heap_sort(s):
    heapify(s)
    rest(s)
    return s 

def heapify(s):
    start = (len(s)-2)//2

    while start >= 0: 
        sift_down(s,start,len(s)-1)
        start = start - 1

def rest(s):
    end = len(s)-1
    
    while end >0: 
        swap(s,end,0)
        end = end -1
        sift_down(s,0,end)

def sift_down(s,start,end):
    root = start
    child = root * 2 +1
    
    while child <= end: 
        if child + 1 <= end and s[child] <= s[child+1]: 
            child = child +1
        if s[root] < s[child]:
            swap(s,root,child)
            root = child
        else: return 
        

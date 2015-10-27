import random 

def quick_sort(s): 
    less = []
    equal = []
    more = []
    i = 0
    
    if len(s) <= 1: return s
    else: 
        pivot = random.randrange(len(s))
        while i < len(s): 
            if s[i] < s[pivot]: 
                less.append(s[i])
            elif s[i] > s[pivot]: 
                more.append(s[i])
            else: 
                equal.append(s[i])
            i = i+1
        less = quick_sort(less)
        more = quick_sort(more)
        return more + equal + less 

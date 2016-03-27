def count1(s, value): 
    total = 0
    for i in s:
        if i == value:
            total = total + 1
    return total

def count2(s, value): 
    i, total = 0,0
    while i< len(s): 
        if s[i] == value: 
            total = total +1
        i = i+1
    return total 

def remove(s): 
    i,j = 0, 0
    new_array = []
    item = s[0]-1
    while i < len(s): 
        if s[i] != item: 
            new_array.append(s[i])
        item = s[i]
        i = i+1
    return new_array

def buble_sort(s): 
    temp = 0
    for i in range(len(s)): 
        for j in range(len(s)-1,i+1,-1): 
            if s[j] < s[j-1]: 
                temp = s[j]
                s[j] = s[j-1]
                s[j-1] = temp
    return s

def remove_sort(s): 
    return remove(buble_sort(s))
    

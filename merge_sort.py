def merge_sort_iter(s): 
    if len(s) <= 1: return s
    mid = len(s)//2
    left_array = s[:mid]
    right_array = s[mid:]

    merge_sort_iter(left_array)
    merge_sort_iter(right_array)

    i,j,k = 0,0,0

    while i<len(left_array) and j< len(right_array): 
        if left_array[i] < right_array[j]: 
            s[k] = left_array[i]
            i = i+1
        else: 
            s[k] = right_array[j]
            j = j +1
        k = k +1

    while i < len(left_array): 
        s[k] = left_array[i]
        k = k +1
        i = i+1
        
    while j < len(right_array): 
        s[k] = right_array[j]
        k = k+1
        j = j+1

    return s

def merge_sort_recursive(s): 
    if len(s) <= 1: return s
    else: 
        mid = len(s)//2
        left = merge_sort_iter(s[:mid])
        right = merge_sort_iter(s[mid:])
        result = merge(left,right)
    return result 

def merge(left,right):
    if len(left) == 0: return right
    if len(right) == 0: return left
    if left[0] < right[0]: 
        return [left[0]] + merge(left[1:], right)
    return [right[0]] + merge(left,right[1:])

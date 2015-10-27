def insertion_sort(s): 
    for i in range(1,len(s):
        k = i
        while k > 1 and s[k] < s[k-1]: 
            temp = s[k]
            s[k] = s[k-1]
            s[k-1] = temp 
            k = k-1
    return s

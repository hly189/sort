from swap import swap 

def insertion_sort(s): 
    for i in range(1,len(s):
        k = i
        while k > 1 and s[k] < s[k-1]: 
            swap(s,k,k-1)
            k = k-1
    return s

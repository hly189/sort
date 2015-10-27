def bubble_sort(s):
    temp = 0
    for i in range(len(s):
        for j in range(len(s)-1, i,-1):
            if s[j] < s[j-1]:
                temp = s[j]
                s[j] = s[j-1]
                s[j-1] = temp

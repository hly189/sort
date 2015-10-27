def selection_sort(s):
    k = 0
    for i in range(len(s)):
        k = i
        for j in range(i+1, len(s)-1):
            if s[j] < s[k]:
                k = j
        temp = s[i]
        s[i] = s[k]
        s[k] = temp
    return s

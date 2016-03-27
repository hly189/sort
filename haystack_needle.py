def strStr(haystack, neddle): 
	if len(haystack) < len(neddle): return None 
	i = 0

	while i < len(haystack) - len(neddle) + 1: 
		j = 0
		k = i 
		while j < len(neddle): 
			if haystack[k] == neddle[j]: 
				j = j + 1
				k = k+1
			else: 
				break 
		if j == len(neddle):
			break
		else: 
			i = i + 1
	if i == len(haystack) - len(neddle) + 1: 
		print("no substring")
	else: 
		return haystack[i:

		]


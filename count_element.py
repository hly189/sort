from counting import remove
from quick_sort import quick_sort
import random 

def counting_element(s): 
	#if array is empty, force quit 
	if len(s) == 0: return 

	#sorted an array 
	s = quick_sort(s)

	previous = s[0]
	count = 0
	new_array = []
	new_array.append(count)
	j = 0

	for i in range(0,len(s)): 
		if s[i] == previous: 
			count = count + 1
			new_array[j] = count 
		else: 
			print("element:{0},appear:{1}".format(previous,count))
			previous = s[i]
			count = 1
			j = j + 1
			new_array.append(count)
	print("element:{0},appear:{1}".format(previous,count))
	return new_array

def remove_sort(s): 
	s = remove(quick_sort(s))
	return s 

def put_to_dict(s1,s2): 
	dictionary = dict()


s = [1,3,2,4,2]
#s = quick_sort(s)
#a = counting_element(s)
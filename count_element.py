from counting import remove
from quick_sort import quick_sort
import random 

"""
This function will be used to count repeated element in an array 
The return will be an array of count number, and it will also print 
out each element of array and repeated time of that element
"""
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

"""
This function will sort an array and deleted the duplicated of an element that array 
"""
def remove_sort(s): 
	s = remove(quick_sort(s))
	return s 

"""
This function is used to map 2 arrays into a dictionary
"""
def put_to_dict(s1,s2): 
	dictionary = dict(zip(s1,s2))
	return dictionary

"""Return the kth element which have the most repeated times in an array"""
def max_kth_element(s):
	count_element = counting_element(s)
	s = remove_sort(s)
	dictionary = put_to_dict(s,count_element)
	inverse = [(value, key) for key, value in dictionary.items()]
	max_key = max(inverse)[1]
	return max_key



s = [1,3,4,4,3,2,2,2,5,6,7,7]
max = max_kth_element(s)
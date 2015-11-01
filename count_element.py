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

	#sort an array 
	s = quick_sort(s)

	previous = s[0] # set previous to the first element in that array 
	count = 0 # count is used to keep track of the element 
	new_array = [] #this array is used to store the count elemnt 
	new_array.append(count) #create first element of empty array 
	j = 0 

	#go through the array and find the repeated elemnt of that aray
	for i in range(0,len(s)): 
		if s[i] == previous: 
			count = count + 1
			new_array[j] = count 
		else: 
			print("element:{0},appear:{1}".format(previous,count))
			previous = s[i] # set previous to the next element 
			count = 1 #reset this couting to 1
			j = j + 1 # move to the next element of new_array
			new_array.append(count) # append to the next count of new element 
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

def return_k_element(s,k): 
	count_element = counting_element(s)
	s = remove_sort(s)
	dictionary = put_to_dict(s,count_element)
	dictionary2 = quick_sort([(value,key) for  (key,value) in dictionary.items()])

	array_k = []
	i = 0

	while i <k: 
		array_k.append(dictionary2[i][1])
		i = i+1

	return array_k



s = [1,3,4,4,3,2,2,2,5,6,7,7]
a = return_k_element(s,3)
#a = counting_element(s)
#s = remove_sort(s)
#dictionary = put_to_dict(s,a)
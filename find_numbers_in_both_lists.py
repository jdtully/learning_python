#find numbers  in  both lists
lst1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
lst2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# Python program to illustrate the intersection 
# of two lists using set() method 
def intersection(lst1, lst2): 
	return set(lst1) & set(lst2)

# Driver Code 
#lst1 = [15, 9, 10, 56, 23, 78, 5, 4, 9] 
#lst2 = [9, 4, 5, 36, 47, 26, 10, 45, 87] 
print(list(intersection(lst1, lst2))) 





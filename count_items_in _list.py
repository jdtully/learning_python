     #new function,  count items in list (2,list with 222 5)  get return of 3
def count_items_in_list(list):
    counts=dict()
    for i in list:
        if i in counts:
            counts[i] += 1
        else: 
            counts[i] = 1
    return counts
list=[1, 1, 1, 2, 5, 3, 1, 3, 6, 1, 4, 4, 4, 8, 2, 2, 2] 
print(count_items_in_list(list))




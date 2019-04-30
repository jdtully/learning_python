#Multiply all the numbers  In a list
def find_the_product_of_list(list):
    totaler = 1
    
    for i in (list):
        totaler = totaler*i
    return totaler
list = [1,6,8,6,21,12]    
print(find_the_product_of_list(list))

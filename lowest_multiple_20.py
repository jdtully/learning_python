import math
def find_divisors(number):
    try:
        number + 0
    except:
        print("Not a number")
    num_list = []
    for i in range(1,int(math.sqrt(number))+1):
        if number%i == 0:
            num_list.append(i)
            num_list.append(int(number/i))
    return num_list

def is_prime(number): 
    for i in range(2,int(math.sqrt(number))+1): 
        if number % i == 0: 
            return False
    return True

def get_biggest_prime(num_list):
    biggest_num=int()
    for i in num_list:
        if is_prime(i):
            if i > biggest_num:
                biggest_num = i
    return biggest_num


def get_primes_below(number):
    primelist=[]
    for i in range(2,(number+1)):
        if is_prime(i): 
            primelist.append(i)
    return primelist    

# start with range 1-> input
# check  for prime = add prims  to list
# skip not primes
#return list of primes


#get_prime_factorization recursive
def get_factorization(number):
    factlist=[]
    if is_prime(number):
        factlist.append(number)
        return factlist   
    entered = number
    primelist=get_primes_below(int(math.sqrt(number))+1)
    for i in primelist:
        if number%i == 0: 
            factlist.append(i)
            factor=int(number / i)
            if factor > 1:
                next_factorization = get_factorization(factor)
                factlist = factlist + next_factorization
                return factlist
    return factlist

#Multiply all the numbers  In a list
def find_lcm_for_range(r):
    list_of_factors=get_factorisations_for_range(r)
    lcm_factors=dict()   
    for k in list_of_factors.keys():
        #getfactorization  for K
        current_factors=list_of_factors[k]
        counts=count_items_in_list(current_factors)
        for ck in counts.keys():
            if ck in lcm_factors:
                if lcm_factors[ck]<counts[ck]:
                    lcm_factors[ck] = counts[ck]
            else:
                lcm_factors[ck]=counts[ck]  

        return lcm_factors

#new function,  count items in list (2,list with 222 5)  get return of 3
def count_items_in_list(factors_list):
    counts=dict()
    for i in factors_list:
        if i in counts:
            counts[i] += 1
        else: 
            counts[i] = 1
    return counts
#factors_list=[1, 1, 1, 2, 5, 3, 1, 3, 6, 1, 4, 4, 4, 8, 2, 2, 2,7] 
#print(count_items_in_list(factors_list))

#get factorizations for 
def get_factorisations_for_range(r):
    list_of_factors=dict()
    for i in r:
        list_of_factors[i]=get_factorization(i)
    return list_of_factors



#list = [1,2,3,4,5]
#r=[1, 1, 1, 2, 5, 3, 1, 3, 6, 1, 4, 4, 4, 8, 2, 2, 2,7] 

number = int(input("Enter a number:  "))
num_list = find_divisors(number)
no_primes = [6,26,48,55]
print("get_primes\n",get_primes_below(number))        
print("get_factorization\n",get_factorization(number))
print("find_lcm_for_range\n",find_lcm_for_range(range(2,number+1)))
print("count_items_in_list\n",count_items_in_list(factors_list))
print("get_factorisations_for_range",get_factorisations_for_range(range(2,number+1)))
#print("get_product_of_count",get_product_of_count(list)))




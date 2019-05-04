import math
#This function takes a number  and  returns  all the divisors
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

#This function figures whether a number is prime
def is_prime(number): 
    for i in range(2,int(math.sqrt(number))+1): 
        if number % i == 0: 
            return False
    return True

#This function  gets  the list of prime numbers and  decides which is the largest prime number
def get_biggest_prime(num_list):
    biggest_num=int()
    for i in num_list:
        if is_prime(i):
            if i > biggest_num:
                biggest_num = i
    return biggest_num

#This function takes a list of prime numbers  below a stated threshold

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


#This function breaks out the prime factors  of a composite number
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

#Find smallest number is divisible by all the items in the list.
def find_lcm_for_range(r):
    list_of_factors=get_factorizations_for_range(r)
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

#This function  goes through  a a dictionary and counts how many time each value appears through all the  keys
def count_items_in_list(factors_list):
    counts=dict()
    for i in factors_list:
        if i in counts:
            counts[i] += 1
        else: 
            counts[i] = 1
    return counts


#get factorizations for 
def get_factorizations_for_range(r):
    list_of_factors=dict()
    for i in r:
        list_of_factors[i]=get_factorization(i)
    return list_of_factors

#count items in list for dictionary ( get factorization for range  to  countable list)
def count_items_in_list_for_dictionary(dictionary):
    for key,val in dictionary.items():
        dictionary[key]=count_items_in_list(val)
    return dictionary

#look at count occurences  and  find largest  set

def tabulate_occurences(factorizations_exp):
    biggest_exp=dict()
    for num,factorization in factorizations_exp.items():
        for p,e in factorization.items():
            if p in biggest_exp:
                if biggest_exp[p]<e:
                    biggest_exp[p]=e
            else:
                biggest_exp[p]=e

    return biggest_exp

def get_product_of_count(biggest_exps):
    totals = 1
    for key, val in biggest_exps.items():
        num= key**val
        totals=totals*num
    return totals    



number = int(input("Enter a number:  "))
num_list = find_divisors(number)
myrange=range(2,number+1)
factorizations = get_factorizations_for_range(myrange)
print("get_primes\n",get_primes_below(number))        
print("get_factorization\n",get_factorization(number))
print("find_lcm_for_range\n",find_lcm_for_range(myrange))
print("count_items_in_list\n",count_items_in_list(factorizations[16]))
print("count examples occurences of  mutipliers\n",count_items_in_list_for_dictionary(factorizations))
print("get_factorizations_for_range\n",factorizations)
print("which exp is  biggest?\n",tabulate_occurences(factorizations))
print("The LCM is ...\n",get_product_of_count(tabulate_occurences(factorizations)))




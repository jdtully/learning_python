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

number = int(input("Enter a number:  "))
num_list = find_divisors(number)
no_primes = [6,26,48,55]
print(num_list)        
print(get_biggest_prime(num_list))



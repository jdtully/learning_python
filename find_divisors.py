import math
#find divisors of  given  number
num_list = []
number = int(input("Enter a number:  "))
#build List
#print(list(nums))
for i in range(1,int(math.sqrt(number))+1):
    if number%i == 0:
        num_list.append(i)
        num_list.append(int(number/i))
print(num_list)



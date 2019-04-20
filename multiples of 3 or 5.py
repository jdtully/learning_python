# we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

#Find the sum of all the multiples of 3 or 5 below 1000.
stop=(1000)
tot = (0)
threes = (0)
tot3=int(0)
tot5=int(0)
for i in range(0,1000):
    if (i%3==0):
        tot3=tot3+i
    elif (i%5==0):
        tot5=tot5+i
print(tot3+tot5)
   
    
    


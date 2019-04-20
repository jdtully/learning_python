
from random import randint
iter = int(0)
tot = int()
need_num = True

while need_num == True:

    try:
        iter = int(input("Please enter a number between 1 and 1,000,000:  "))
        need_num = False
    except:
        print("You are tryna be silly!")
    #break#what is  the average of 1000 random numbers


largest_num = int(0)
for i in range(iter):
    num = randint(1,5000)
    if num >= largest_num:
        largest_num = num
    tot = tot + num
    print(i)
print(tot/iter)
print(largest_num)
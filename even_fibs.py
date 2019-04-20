#calculate fibonac
nums=[]

def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return(fib(n-1)+fib(n-2))
    return n
print(fib(30))


def even_nums(n):
    ##nums=[]
    for i in range(n):
        if i % 2 == 0:
            nums.append(i)
            i=i+1
    return(nums)        
print(even_nums(40))




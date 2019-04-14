fib_cache={}
""" where are the new bits  getting appended  to the dictionary??"""

def fib_rec(n):
    #check for number in cache
    if n in fib_cache:
        return fib_cache[n]

    # Base case
    if n == 1:
        fib_num = 0
    elif n == 2:
        fib_num = 1
    # Recursive case
    elif n > 2:
        fib_num = (fib_rec(n-1) + fib_rec(n-2))
    fib_cache[n] = fib_num
    return fib_num
for n in range(1,1000):
    print(n, ":", fib_rec(n))
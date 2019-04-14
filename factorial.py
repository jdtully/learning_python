def tracer(fn):
    def traced(x):
        print("Before, Calling" ,fn,"(",x,")")
        result=fn(x)
        print("After, Got" ,result,"from" ,fn, "(",x,")")
        return result
    return traced

def fact(n):
    if n ==0:
        return 1
    return n * fact(n-1)
new_fact = tracer(fact)
new_fact(9)





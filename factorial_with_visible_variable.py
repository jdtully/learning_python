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
    fact_n_minus_1_result=fact(n-1)
    return n * fact_n_minus_1_result
new_fact = tracer(fact)
new_fact(15)





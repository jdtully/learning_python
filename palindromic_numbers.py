#A palindromic number reads the same both ways. The largest palindrome made 
# from the product of two 2-digit numbers is 9009 = 91 × 99.

#Find the largest palindrome made from the product of two 3-digit numbers.
def biggest_pal(n1,n2):   
    biggest = int(0)
    for m1 in range(n1,n2):
        for m2 in range(n1,n2):
            prods = m1 * m2
            if str(prods) == str(prods)[::-1]:
                if prods > biggest:
                    biggest=prods
                    return biggest
print(biggest_pal(100,999))
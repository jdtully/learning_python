def get_product_of_count(c):
    totals = 1
    for key, val in c.items():
        num= key**val
        totals=totals*num
    return totals

c={2:3,3:4,5:4,7:5,11:2}

print(get_product_of_count(c))
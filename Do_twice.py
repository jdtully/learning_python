def add(x, y):
  return x + y

def mul(x,y):
  return x * y  



def do_twice(bob, x, y):
  return bob(bob(x, y), bob(x, y))

a = 5
b = 10

print(do_twice(mul, a, b))
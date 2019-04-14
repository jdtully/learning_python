#What is the output of this code?
def test(mult, arg):
  return mult(mult(arg))

def mult(x):
  return x * x

print(test(mult, 2))
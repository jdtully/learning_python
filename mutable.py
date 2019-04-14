# The explanation to immutable and mutable objects of Python3

foo = list(range(4, -1, -1))
print(foo, "output of foo")

bar = list(range(5)[::-1])
print(bar, "output of bar\n")

print(foo == bar, end="")
print(", foo == bar")

if foo is bar:
    print("Yep, they are the same thing with different names." + "\n")
else:
    print("But, they have different ids due to different memory spaces.\n")

print(id(foo), "<-- foo's id")
print(id(bar), "<-- bar's id\n")

# Look at the difference below:

# mutable objects
baz = list(range(4, -1, -1))
print(baz, "output of baz")
print(id(baz), "<-- baz's id, it differ from foo and bar though it is defined by the same function with foo.\n")

qux = foo
print(qux, "output of qux")
print(id(qux), "<-- qux's id, it's same as foo.\n")

qux += [5]
print(qux, "qux now")
print(id(qux), "<-- id of qux is not changed")
print(foo, "foo is also changed due to mutable memory space")
print(id(foo), "<-- id of foo is not changed\n")

# We should know:
# x += [m] is not x = x + [m].
# x is still x after doing the statement x += [m], but value changes in memory space.
# x is not the previous x after doing the statement x = x + [m], it is a new object with different id. The previous one(memory space) will be exterminated by Python's Auto Garbage Collection Mechanism if there is no references to it.
foobar = bar
print(foobar, "output of foobar, same as bar.")
print(id(foobar), "<-- id of foobar, it has the same object reference as bar.\n")

foobar = foobar + [6, 7]
print(foobar, "foobar now, it chages")
print(id(foobar), "<-- id of foobar now, a new one")
print(bar, "bar now, same as the previous one.")
print(id(bar), "<-- id of bar now, no changes.\n")

# immutable objects
a = 321.863
b = 321.863
c = a

print(a, "output of a, b, c")
print(id(a),"<-- id of float number a")
print(id(b), "<-- id of float number b")
print(id(c), "<-- id of float number c\n")

a += 1000

print(a, "a now, surely changes")
print(id(a), "<-- id of a, it is changed by creating a new memory space.")

print(c, "c now, no changed by a.")
print(id(c), "<-- id of c, still same as the previous one.")

print(b, "b now, no changes.")
print(id(b), "<-- id of b")
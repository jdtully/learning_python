filename = input("Enter a filename: ")

with open(filename) as f:
   text = f.read()

print(text)
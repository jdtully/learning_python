def decor(func):
  print("============")
  func()
  print("============")

@decor
def print_text():
  print("Hello world!")

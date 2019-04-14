num1 = 0
num2 = 0
rich = False

def get_nums():
    global num1
    global num2
    num1 = float(input("Please enter your payrate: "))
    num2 = float(input("Please enter your hours: "))

while True:
    get_nums()
    if num2 <= float(40):
        print(num1*num2)
        break
    elif num2 > float(40):
        print((((num2-40)*1.5)+40)*num1)
        break

    else:
        print("Unknown input")

        
        

num1 = 0
num2 = 0
rich = False

def get_nums():
    global num1
    global num2
    num1 = float(input("Please enter your payrate: "))
    num2 = float(input("Please enter your hours: "))

while True:
    print("Do you want to calculate your check? y/n:")
    user_input = input(": ")

    if user_input == "n":
        break
    else:
        get_nums()
        if user_input == "y" and num2 <= float(40):
            result = (num1 * num2)
        elif user_input == "y" and num2 > float(40):
            result = ((((num2-40)*1.5)+40)*num1)
            rich = True
        else:
            print("Unknown input")

        
        
        print("The answer is ",result)
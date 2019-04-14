num1 = 0
num2 = 0

def get_nums():
    global num1
    global num2
    num1 = float(input("payr: "))
    num2 = float(input("Enter another number: "))

while True:
    print("Please enter your pay rate and hours:")
    user_input = input(": ")

    if user_input == "quit":
        break
    else:
        get_nums()
        if user_input == "add":
            result = (num1 + num2)
        elif user_input == "subtract":
            result = (num1 - num2)
        elif user_input == "multiply":
            result = (num1 * num2)
        elif user_input == "divide":
            result = (num1/num2)
        else:
            print("Unknown input")
        
        print("The answer is ",result)
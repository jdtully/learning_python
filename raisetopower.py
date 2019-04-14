def raise_to_power(num,exp_num):
    result = 1
    index = 0
    while index < exp_num:    
        result = result*num
        index +=1
    return(result)

def get_int_input(prompt):
    value=0
    successful_input = False
    while not successful_input:
        try:
            value=int(input(prompt))
            successful_input = True
        except:
            print("Please use a number")
    return(value)

num = get_int_input("Enter a number: ")
exp_num = get_int_input("Enter the exponent: ")

print(raise_to_power(num,exp_num))
    


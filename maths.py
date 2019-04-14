#is it hot outside?
#get temp from user

keys=("F","C")
scale=str()
temp_f=()
temp=()
while True:
    try:
        temp=float(input("What is the temperature outside?  "))
        break
    except ValueError:
        print("That wasn't a number")
while True:
    try:
        f_or_c=str(input("Was that (F)ahrenheit or (C)elcius?  ")).upper()
        if f_or_c in keys:
            scale = f_or_c
            break
    except ValueError:
        print(" F OR C Please")
if scale == "C":
#yes i stole the converter
    temp_f = 9.0/5.0 * temp + 32
else:
    temp_f=temp
if temp_f >= 100:
    print("Damn, its Houston hot")
elif temp_f >= 90:
    print("Welcome South Brother")
elif temp_f >= 75:
    print("Now we are talking")
elif temp_f >= 65:
    print("Better grab a jacket")
else:
    print("Hell hath frozen over and our death is nigh!!")


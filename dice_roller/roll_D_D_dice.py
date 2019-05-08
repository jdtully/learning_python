#roll multiple dice in python like d&dice
import random
check_dice = (4,6,8,10,20)
roll_again="yes"
def roll_dice(sides,rolls):
    turn = list()
    for i in range(rolls):
        roll = random.randint(1, sides)
        turn.append(roll)      
    return turn


roll_again = "yes"
result=list()
while roll_again == "y" or roll_again == "Y" or roll_again =="yes" or roll_again == "Yes":
    perc=input("Is this a percentage roll?(Y)es or (N)o")
    if "Y" in perc or "y" in perc:
        sides = 10
        rolls = 2
        result = roll_dice(sides,rolls)
    else:
        sides=input("how many sides do the dice have? 4,6,8,10 or 20?..")
        try:
            sides = int(sides)   
        except ValueError:
            print("That wasn't a valid Dice!")
            continue
        if sides in check_dice:
            rolls=int(input("how many dice are  we rolling?"))
            result = roll_dice(sides,rolls)
        else:
            print("There isnt a die with",sides,"sides!")
            continue
    print("You Rolled",result)
    roll_again=input("Do you want to roll again?")     




    


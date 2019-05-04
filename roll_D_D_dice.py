#roll multiple dice in python like d&dice
import random
check_dice = (4,6,8,10,20)
roll_again="yes"
def roll_dice(sides,rolls):
    turn = list()
    while rolls > 0:
        roll = random.randint(1, sides)
        turn.append(roll)
        rolls = rolls - 1
        
    #print(turn)
    return turn


if roll_again == "y" or roll_again == "Y" or roll_again =="yes" or roll_again == "Yes":
    roll_again = "yes"
    roll_again=input("Do you want to roll the dice?")      
    while roll_again == "yes":
    perc=input("Is this a percentage roll?(Y)es or (N)o"):
        if "Y" in perc or if "y" in perc:
            sides = 10
            rolls = 2
            roll_dice(sides,rolls)
            perc = "n"
    #  else:
        sides=input("how many sides do the dice have? 4,6,8,10 or 20?..")
        try:
            sides = int(sides)   
        except ValueError:
            print("That wasn't a valid Dice!")
        if sides in check_dice:
            rolls=int(input("how many dice are  we rolling?"))
            roll_dice(sides,rolls)

        else:
            print("You have a die with",sides,"sides?")
        print("You Rolled",(roll_dice(sides,rolls)))
        roll_again




    


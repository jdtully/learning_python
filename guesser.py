
"""Guess a number within a range.
Exercises
1. Change the range to be from 0 to 1,000,000.
2. Can you still guess the number?
3. Print the number of guesses made.
4. Limit the number of guesses to the minimum required.
"""

from random import randint

start = 1
end = 100
value = randint(start, end)
tries = 0

print(value)
print("I'm thinking of a number between", start, "and", end)

guess = None

while guess != value:
    text = input("Guess the number: ")
    guess = int(text)
    tries = tries + 1
    if guess < value:
        print("Higher.")  
    elif guess > value:
        print("Lower.")
end

if tries == 1:
    print("you got it on the first try!")
elif tries > 1:
    print("It only took you", tries, "tries")
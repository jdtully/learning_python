secret_word = "giraffe"
guess=""
tries = 0
limit = 3
out_of_tries = False

while guess != secret_word and not out_of_tries:
    if tries < limit:
        guess=input("name a word ")
        tries +=1
    else:
        out_of_tries = True
        print("loser!!")

if out_of_tries:
    print("loser!")
else:
    print(" winner ")

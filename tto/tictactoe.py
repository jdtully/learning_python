#play tictactoe
#pick player 1 and player 2
# define grid
winner = False
grid = [1,2,3,4,5,6,7,8,9]
xplays = []
oplays = []
turn = "X"
#declare  start of play (x goes first? )
#accept numbers  from player
#remove number from available list
#test for winner
def ifwinner(plays):
    win=False
    winners=[[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
    splays=set(plays)
    for wincom in winners:
        swin = set(wincom)
        if swin.issubset(splays):
            win=True
    return win
while not winner:
    if len(grid) == 0:
        print("game is tied")
        break
    print(grid)
    play=input("What spot do you want?")
    try:
        num=int(play)
        if num > 9 or num < 1:
            print("Thats out of range!")
            continue
    except(ValueError):
        print("That wasn't even a number!")
        continue
    if play in grid:
        grid.remove(play)
    else:
        print("That spot is unavailable")
        continue
    if turn == "X":
        xplays.append(play)
        if ifwinner(xplays):
            print("The winner is ",turn," with",xplays) 
            break
        turn = "O"
        print("It's",turn,"'s turn")
    else:
        oplays.append(play)
        if ifwinner(oplays):
            print("The winner is ",turn," with",oplays)
            break
        turn = "X"
        print("It's",turn,"'s turn")
    
    print("X has",xplays,"O has",oplays)

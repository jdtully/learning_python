#calculate steps
import random
    x = 0
    y = 0
def Random_walk(n):
#return coordinates  after   random walking steps
    for i in range(30):
        step=random.choice(['N','S','E','W'])
        if step == 'N':
            y=y+1
        elif step == 'S':
            y=y-1
        elif step == 'E':
            x=x+1
        else:
            x=x-1
    for i in range(25):
        walk=Random_walk(10)
        print(walk, "distance from home", abs(walk[0])+abs(walk[1]))

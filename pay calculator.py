#written from scratch

pay = input("What is the payrate? ")
pay=float(pay)
mult = float(1.5)
net_time = float(0)
def figure_time():
    hours = float(input("How many hours did you work ? "))
    base=float()

    if (hours <= 40):
        base = hours
    elif (hours > 40):
        base = (((hours-40)*mult)+40)
    return(base)
print(pay*figure_time())



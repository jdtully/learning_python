#written from scratch
time1=float
rate1=float

def get_time_rate():
    global time1
    global rate1
    time1 = float(input("How many hours did you work? "))
    rate1 = float(input("How much do you make an hour? "))

pay=float()
mult = float(1.5)
net_time = float()
hours=float()
base=float()
base_time=float(40)

if (time1 =< base_time):
    base = time1
    print(base*pay)
else :
    base = (((time1-40)*mult)+40)
    print(base*pay)




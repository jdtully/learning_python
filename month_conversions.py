months = {
    "jan":"January",
    "feb":"February",
    "mar":"March",
    "apr":"April",
    "may":"May",
    "jun":"June",
    "jul":"July",
    "aug":"August",
    "sep":"September",
    "oct":"October",
    "nov":"November",
    "dec":"December",
    
}
months["wop"] = "Whopper"
month = input("Name a month ")
monthlower = month.lower()
if monthlower in months.keys():
    print(months[monthlower])
else:
    print("you suck")

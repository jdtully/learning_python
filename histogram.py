name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
counts = dict()
#biggest = int(0)
bigname = str()
#name_l = list()
for line in handle:
    if not line.startswith("From: "):continue
    l_clean = line.split()[1]
    if l_clean not in counts:
        counts[l_clean] = 1
    else:
        counts[l_clean] = counts[l_clean] +1
for name in counts:
    if bigname == "":
        bigname = name
    if counts[name] >= counts[bigname]:
        bigname = name
print(bigname,counts[bigname])

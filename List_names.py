fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
fh = open(fname)
#line = str()
count = 0
for line in fh:
    if not line.startswith("From: ") : continue
    s_line = list((line.split()))
    l_clean = (s_line[1])
    count = count + 1
    print(l_clean)


print("There were", count, "lines in the file with From as the first word")
name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)


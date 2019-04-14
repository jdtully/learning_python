count = 0
tot = 0
ans = 0
# Use the file name mbox-short.txt as the file name
#fname = input("Enter file name: ")
fname = ("mbox-short.txt")
fh = open(fname,'r')
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    count = count + 1
    num = float(line[line.find(":") + 1 : ])
    
    tot = num + tot
ans = tot / count    
print ("Average spam confidence:",ans)
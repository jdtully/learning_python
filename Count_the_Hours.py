hour_pos = 5
name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
counts = dict()
for line in handle:
    if not line.startswith("From "):continue
    #why is  the colon  import
    l_clean = line.split(':')[0]
    for word in l_clean:
            clean_word = l_clean.split()[hour_pos]
            break
    if clean_word not in counts:
        counts[clean_word] = 1
    else:
        counts[clean_word] = counts[clean_word] +1
#sort_cl_wo= sorted(counts.items())
for k,v in sorted(counts.items()):
    print(k,v)
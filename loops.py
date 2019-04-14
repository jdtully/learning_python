
fname = input("Enter file name: ")
fname = ("romeo.txt")
fh = open(fname)
#bring file into list
text = []
for line in fh:
	words = line.split()
    # looks through each item in the list
	for word in words:
        # if the item is in the list "words" it is skipped, otherwise it is added	
		if word in text : continue
		else:
			text.append(word)
# sorts the list in alphabetical order and prints
print(sorted(text))




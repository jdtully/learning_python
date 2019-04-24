import re
handle = open("genesis.txt")
verse_delimiter = ('[0-9]+:[0-9]+')
p_bible=dict()
#put in string to avoid  error
current_verse="start"
for line in handle:
    verse_nums = re.findall(verse_delimiter,line) 
    rest_of_line=line
    if len(verse_nums)==0:
        p_bible[current_verse]=p_bible[current_verse]+ line
    for verse_num in verse_nums:
        parts=rest_of_line.partition(verse_num)
        if current_verse in p_bible:
            p_bible[current_verse]=p_bible[current_verse]+parts[0]
        else:
            p_bible[current_verse]= parts[0]
        if current_verse != verse_num:
            current_verse=verse_num
        rest_of_line=parts[2]
    if current_verse in p_bible:
        p_bible[current_verse]=p_bible[current_verse]+rest_of_line
    else:
        p_bible[current_verse]=rest_of_line
print(p_bible["1:17"])
            




import re
handle = open("Genesis.txt")
verse_delimiter = ('[0-9]+:[0-9]+')
current_verse = str()
previous_verse = int()
frag=str()
p_bible = dict()
p_bible_data_to_update = ()
for line in handle:
    #case 1 line startes  with  verno
    verse_nums = re.findall(verse_delimiter,line)
#if  there  is 1 example of  the string
    if len(verse_nums) == 0:    
        verse_nums = re.findall(verse_delimiter,line) 
    rest_of_line=line 
    for verse_num in verse_nums:
        parts=rest_of_line.partition(verse_num)
        p_bible[current_verse]=p_bible[current_verse]+parts[0]
        if current_verse != verse_num:
            current_verse=verse_num
        rest_of_line=parts[2]
    p_bible[current_verse]=p_bible[current_verse]+rest_of_line
            



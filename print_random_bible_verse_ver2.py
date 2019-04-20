import re
handle = open("Genesis.txt")
verse_delimiter = ('[0-9]+:[0-9]+')
current_verse = str()
previous_verse = int()
line_text_clean = ()
line_text_lfrag = ()
line_text_rfrag = ()
p_bible = dict()
p_bible_data_to_update = ()
for line in handle:
    #case 1 line startes  with  verno
    verse_nums = re.findall(verse_delimiter,line)
    #print(lwords)
    if len(verse_nums) == 1:
        if re.match(verse_delimiter,line):
            if verse_nums[0]!= current_verse:
                vers_nums_length = len(verse_nums[0])+1
                line_text_clean = line[vers_nums_length:]
                p_bible[verse_nums[0]] = line_text_clean
                current_verse = verse_nums[0]
        elif re.search(verse_delimiter,line):
            if verse_nums[0]!= current_verse:
                #vers_nums_length = len(verse_nums[0])+1
                line_text_clean=line.split(verse_delimiter)[0]
                p_bible[verse_nums[0]] = line_text_clean
                current_verse = verse_nums[0]
                p_bible[verse_nums[0]] = line_text_clean
            previous_verse = verse_nums[0]
                #use  string search  to find  position and  extract
                #chars  to the  beginnng of  the line
                #then check  after  string for more txt  and
                #add it to the dictionary  with new index

        #case 2 line  has  no ver no
    elif len(verse_nums) == 0:
        p_bible[current_verse] = p_bible[current_verse] + line
    #case 3 line has  multiple ver nos
    elif len(verse_nums) > 1:
        pass
    #case 4 line has 1 ver no not  in the beginning
    else:
        pass
    #print(current_verse)






    #parse  the line
    #if re
     
"""name = input("Enter file:")
if len(name) < 1 : name = "regex_sum_213114.txt"
handle = open(name)
import re
nums = float()
totaler =float()
for line in handle:
    f_nums = re.findall('[0-9]+',line)
    if len(f_nums) > 0:
        for num in f_nums:
            nums += int(num)
print(nums)"""

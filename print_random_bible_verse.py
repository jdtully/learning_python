import re
handle = open("Genesis.txt")
current_verse = str()
line_text_clean = ()
line_text_lfrag = ()
line_text_rfrag = ()
p_bible = dict()
p_bible_data_to_update = ()
for line in handle:
    verse_nums = re.findall('[0-9]+:[0-9]+',line)
    #print(lwords)
    if len(verse_nums) == 1:
        if verse_nums[0]!= current_verse:
            vers_nums_length = len(verse_nums[0])+1
            line_text_clean = line[vers_nums_length:]
            p_bible[verse_nums[0]] = line_text_clean
            current_verse = verse_nums[0]
    elif len(verse_nums) == 0:
        p_bible[current_verse] = p_bible[current_verse] + line    
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

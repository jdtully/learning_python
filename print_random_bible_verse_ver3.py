import re
handle = open("Genesis.txt")
verse_delimiter = ('[0-9]+:[0-9]+')
current_verse = str()
previous_verse = int()
p_bible = dict()
p_bible_data_to_update = ()
for line in handle:
    #case 1 line startes  with  verno
    verse_nums = re.findall(verse_delimiter,line)
#if  there  is 1 example of  the string
    if len(verse_nums) != 0:
        for verse_delimiter in line:
            if not line.partition(verse_nums[0]):
                if verse_nums[0]!= current_verse:
                    line_text_clean = line[len(verse_nums[0])+1:]
                    p_bible[verse_nums[0]] = line_text_clean
                    current_verse = verse_nums[0]
#if  the line starts  with the string
        if re.match(verse_delimiter,line):
            if verse_nums[0]!= current_verse:
                line_text_clean = line[len(verse_nums[0])+1:]
                p_bible[verse_nums[0]] = line_text_clean
                current_verse = verse_nums[0]
#if  the string is  in the middle of the line          
        elif re.search(verse_delimiter,line):#
            if verse_nums[0]!= current_verse:
                line_text_clean=line.partition(verse_nums[0])
                p_bible[current_verse] = p_bible[current_verse]+line_text_clean[0]
                current_verse = verse_nums[0]
                p_bible[current_verse] = line_text_clean[2]
#Have to append  the text to the previouse verse
            previous_verse = verse_nums[0]
                #use  string search  to find  position and  extract
                #chars  to the  beginnng of  the line
                #then check  after  string for more txt  and
                #add it to the dictionary  with new index
# if  there  are NO  examples of the string
    elif len(verse_nums) == 0:
        p_bible[current_verse] = p_bible[current_verse] + line
    #case 3 line has  multiple ver nos
    elif len(verse_nums) > 1:
        #partion  the string for each versenum
        #if  the vers num partition 0 is  empty its  at the  beginning 
        #the string.
        
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

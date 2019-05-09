import re
import random
import sqlite3

conn = sqlite3.connect('bible_verse.sqlite')
cur = conn.cursor()


handle = open("genesis.txt")
verse_delimiter = ('[0-9]+:[0-9]+')
p_bible=dict()
#put in string to avoid  error
current_verse="start"
for line in handle:
    verse_nums = re.findall(verse_delimiter,line)
    if len(verse_nums)==0:
            UPDATE bible_verse SET description = 'desc of ' || name
    else:
        rest_of_line=line
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




#table_name = 'test_table'
#attrib_names = ", ".join(dict_data.keys())
#attrib_values = ", ".join("?" * len(dict_data.keys()))
#sql = f"INSERT INTO {table_name} ({attrib_names}) VALUES ({attrib_values})"
#cursor.execute(sql, list(dict_data.values()))  
print(key)
print(p_bible[key])
            




import re
import random
import sqlite3

# insert_data from p_bible to sql table
def insert_data(cur,k,v):
    sql = ('''INSERT INTO bible_verse(chapter,verse)VALUES(?,?)''')
    cur.execute(sql,(k,v))


#put in string to avoid  error

def parse_bible(fname):
    current_verse="start"
    handle = open(fname)
    verse_delimiter = ('[0-9]+:[0-9]+')
    p_bible=dict()
    for line in handle:
        verse_nums = re.findall(verse_delimiter,line)
        if len(verse_nums)==0:
            p_bible[current_verse]=p_bible[current_verse]+ line
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
    return p_bible

def get_and_insert(bible_dictionary):
    conn = sqlite3.connect('bible_proj.db')
    cur = conn.cursor()  
    for key in bible_dictionary.keys():
        verse=bible_dictionary[key]
        insert_data(cur,key,verse)
    conn.commit()
    cur.close()
    print(key)


    
get_and_insert(parse_bible("genesis.txt"))
print("done")




            




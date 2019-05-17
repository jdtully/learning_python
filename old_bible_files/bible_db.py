import sqlite3

conn = sqlite3.connect('bible_verse.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS bible_verse')

cur.execute('''
CREATE TABLE Bible_verse (row_num INTEGER, chap TEXT, verse TEXT)''')
def insert_line(data_insert):
    cur.execute('SELECT verse FROM bible_verse WHERE chap = ? ', (chap,))
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO bible_verse (chap, verse)
                VALUES (?, 1)''', (verse,))
    else:
        cur.execute('UPDATE bible SET chap = chap + 1 WHERE verse = ?',
                    (verse,))
    conn.commit()
    return

fname = input('Enter file name: ')
if (len(fname) < 1): fname = 'genesis.txt'
handle = open(fname)
import re
import random
verse_delimiter = ('[0-9]+:[0-9]+')
p_bible=dict()
#put in string to avoid  error
current_verse="start"
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


    cur.execute('SELECT verse FROM bible_verse WHERE chap = ? ', (chap,))
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO bible_verse (chap, verse)
                VALUES (?, 1)''', (email,))
    else:
        cur.execute('UPDATE bible SET chap = count + 1 WHERE verse = ?',
                    (verse,))
    conn.commit()

# https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()

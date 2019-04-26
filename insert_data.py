#
# insert_data
import sqlite3
def insert_data(k,v):
    conn = sqlite3.connect('bible_proj.db')
    cur = conn.cursor()
    sql = ('''INSERT INTO bible_verse(chapter,verse)VALUES(?,?)''')
    cur.execute(sql,(k,v))
    conn.commit()

chap = "bob"
verse = "235874"
print(insert_data(chap,verse))

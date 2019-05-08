#python to run drugs  application

import sqlite3

#Enter  the user
def EnterAUser(name, gender):
    conn = sqlite3.connect('drug_trak.sqlite3')
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS user (uname VARCHAR(20) NOT NULL, ugender VARCHAR(20) NOT NULL);''')
    cur.execute("insert into user VALUES(?,?);",(name,gender))
    cur.close()
    conn.commit()
    conn.close()

"""Enter a dose
def EnterADose()
    drug=str(input("Drug name?  "))
    time=str(input("When is this dose"))
    Dose=str(input("Dosage?  "))"""

name=str(input("what is your name?  "))
gender=str(input("what is your gender? "))
print(name,gender)
EnterAUser(name,gender)
print("done")


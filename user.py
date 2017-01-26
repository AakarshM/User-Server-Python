import sqlite3
from flask import *
import bcrypt

"""cur = conn.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS john (name TEXT, number TEXT)')
print("Created table");
cur.execute('INSERT INTO \'john\' VALUES (?, ?)', ("name", "maro"))
conn.commit()
print('Inserted data')
cur.close()
"""

conn = sqlite3.connect('./flaskdb.db')
cur = conn.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS users (email TEXT NOT NULL UNIQUE, password TEXT)')
print('Table created')

def create_user(email, hashedpw):
    try:
        cur.execute('INSERT INTO users VALUES (?, ?)', (email, hashedpw))
        conn.commit()
        return "works"
    except:
        print(str(sqlite3.Error))
        return None



#need to use tuple notation for params, and (?) for theplaceholder.
def verify_user(email, encoded_password):
        cur.execute('SELECT password FROM users WHERE email=(?)', (email,)) #get hashedpw
        hashedPassword = cur.fetchone()[0]
        #ret = json.dumps(returnObject)
        comparePassword = bcrypt.checkpw(encoded_password, hashedPassword)
        if comparePassword == False:
            return None
        else:
            return "User authenticated"

def change_password(email):
        cur.execute('SELECT email FROM users WHERE email =  %s' % email)
        returnObject = cur.fetchall()
        print(returnObject)

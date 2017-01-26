import sqlite3
from flask import *
import bcrypt


conn = sqlite3.connect('./flaskdb.db')
cur = conn.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS todo (todos TEXT, user TEXT)')
conn.commit()

def create_todo():
    cur.execute('INSERT INTO todo VALUES (?, ?)', ("name", "user association email"))
    conn.commit()

def retrieve_todo(email):
    cur.execute('SELECT todos FROM todo WHERE user=(?)', (email,))
    r = cur.fetchall()
    #cur.execute('SELECT * FROM todo')
    if not r:
        return "not found"
    else:
        list1 =[];
        for value in r:
            list1.append(value)
        return list1

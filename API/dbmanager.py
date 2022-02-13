import sqlite3 as sq3
import time
DBNAME = "users.db"

# Not intended to be used in normal application cycle
def createDatabase():
    con = sq3.connect(DBNAME)
    cur = con.cursor()
    cur.execute(''' CREATE TABLE users (username text, 
        datecreated text, played real, wins real, losses real, draws real)''')
    con.commit()
    con.close() 
    
def addUser(username: str):
    con = sq3.connect(DBNAME)
    cur = con.cursor()
    result = cur.execute(f'''INSERT INTO users VALUES ('{username}', '{time.time()}', 0, 0, 0, 0)''')
    con.commit()
    con.close()    

def getUsers():
    con = sq3.connect(DBNAME)
    cur = con.cursor()
    result = cur.execute('''SELECT * FROM users ORDER BY datecreated''')
    for row in result:
        print(row)
    con.commit()
    con.close()

def main():
    addUser("Matthew")
    getUsers()

if __name__ == "__main__":
    main()
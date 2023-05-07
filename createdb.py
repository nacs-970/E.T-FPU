import sqlite3
def make_db():
    con = sqlite3.connect("piggy.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS piggy (type TEXT,date DATE,note TEXT,cost REAL)")
    con.commit()
    con.close()

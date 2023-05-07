import sqlite3

db = 'piggy.db'
table = 'piggy'
name = 'E.T - FPU'
con = sqlite3.connect(db) 
cur = con.cursor()

def base():
    print(f" --- {name} --- ")
    cur.execute(f"SELECT SUM(amount) FROM {table} WHERE type = 'Deposit'")
    td = cur.fetchall()
    cur.execute(f"SELECT SUM(amount) FROM {table} WHERE type = 'Withdraw'")
    tw = cur.fetchall()
    cur.execute(f"SELECT COUNT(*) FROM {table}")
    tt = cur.fetchall()
    tdi = td[0][0]
    twi = tw[0][0]
    tti = tt[0][0]
    if tdi is None and twi is None:
        print(" Total transaction : -")
        print(" Total amount : -")
        print(" Total deposit : -")
        print(" Total withdraw : -")
    if tdi is not None or twi is not None:
        if tdi is None:
            tdi = 0
        if twi is None:
            twi = 0
        print(f" Total transaction : {int(tti)}")
        print(f" Total amount : {round(float(tdi) - float(twi),2)}")
        print(f" Total deposit : {round(float(tdi),2)}")
        print(f" Total withdraw : {round(float(twi),2)}")
    print(" --------------------------- ")
    print(" type | date | note | amount")
    print(" --------------------------- ")

def menu():
    base()
    cur.execute(f"SELECT * FROM {table} ORDER BY date DESC LIMIT 10")
    piggys = cur.fetchall()
    for piggy in piggys:
        print(f" {piggy[0]} {piggy[1]} {piggy[2]} {piggy[3]}")

def menu_a():
    base()
    cur.execute(f"SELECT * FROM {table} ORDER BY date DESC")
    piggys = cur.fetchall()
    for piggy in piggys:
        print(f" {piggy[0]} {piggy[1]} {piggy[2]} {piggy[3]}")

def menu_m(command):
    base()
    cur.execute(command)
    piggys = cur.fetchall()
    for piggy in piggys:
        print(f" {piggy}")
def menu_s():
    base()

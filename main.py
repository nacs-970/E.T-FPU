import sqlite3
import datetime
import getopt
import yaml
from sys import argv,exit
from mode import *

with open('config.yml','r') as file:
    data = yaml.safe_load(file)

db = data['name']
table = data['table']

con = sqlite3.connect(db) 
cur = con.cursor()
cur.execute(f"CREATE TABLE IF NOT EXISTS {table} (type TEXT,date DATE,note TEXT,amount REAL)")
con.commit()

# Check
if len(argv) < 2:
    menu()
    exit(0)

# argv
deposit = None
withdraw = None
date = None 
note = None
mode = None
search = None
etable = None
ebase = None

try:
    opts, args = getopt.getopt(argv[1:],'i:w:d:n:m:s:h',['deposit=','withdraw=','date=','note=','mode=','search=','help'])

except getopt.GetoptError: 
    print("Error : Unknow agrument / querry")
    print("Try -h / --help")
    exit(1)

for opt,arg in opts:
    if opt in ('-h','--help'):
        print('-i / --deposit : Deposit a amount of value into database')
        print('-w / --withdraw : Withdraw a amount of value out of database')
        print('-d / --date : Specify a date for deposit or withdraw')
        print('-n / --note : Specify a note for deposit or withdraw')
        print('-m / --mode : Select mode from [ a / all for all transaction, m / man for manually sql command ]')
        print('-s / --search : Search for specify query')
        print('-h / --help : Call for help')
        exit(0)
    elif opt in ('-i ','--deposit'):
        deposit = arg
    elif opt in ('-w','--withdraw'):
        withdraw = arg
    elif opt in ('-d','--date'):
        date = arg
    elif opt in ('-n','--note'):
        note = arg
    elif opt in ('-m','--mode'):
        mode = arg
    elif opt in ('-s','--search'):
        search = arg

# Type amount
itype = None
cost = None
if deposit is not None and withdraw is None:
    itype = str("Deposit")
    cost = float(deposit)
elif deposit is None and withdraw is not None:
    itype = str("Withdraw")
    cost = float(withdraw)
elif deposit is not None and withdraw is not None:
    print("Error : Can't deposit and withdraw at the same time")
    exit(1)

# Date
if date is None:
    now = datetime.datetime.now()
    date = now.strftime("%Y-%m-%d_%H:%M:%S")

# CREATE TABLE {table} (type TEXT,date DATE,note TEXT,cost REAL);
if itype is not None:
    # Commit
    cur.execute(f"INSERT INTO {table} (type,date,note,amount) VALUES (?,?,?,?)",(itype,date,note,cost))
    con.commit()

# Search
if search is not None:
   mode = 'search'
   cur.execute(f"SELECT * FROM {table} WHERE type LIKE '%{search}%' OR date LIKE '%{search}%' OR note LIKE '%{search}%' OR amount LIKE '%{search}%' ORDER BY date DESC") 
   sear_r = cur.fetchall()

# Mode
if mode is not None:
    mode = mode.lower()
    if mode == 'all' or mode == 'a':
        menu_a()
    elif mode == 'man' or mode == 'm':
        menu_m(argv[3])
    elif mode == 'search':
        menu_s()
        print(" Search Result :")
        for sea in sear_r:
            print(f" {sea[0]} {sea[1]} {sea[2]} {sea[3]}")
    else:
        print("Error : Unknow mode")
else:
    menu()

import sqlite3
from model.model_check_DB import *

def exec_get_items():
    for row in c.execute('SELECT * FROM items'):
        print(row)
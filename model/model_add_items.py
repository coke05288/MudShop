import sqlite3
from model.model_check_DB import *

def exec_add_items(itemData):

    id = itemData[0]
    name = itemData[1]
    price = itemData[2]
    quantity = itemData[3]

    c.execute('INSERT INTO items VALUES(?, ?, ?, ?, ?)', (id, name, price, quantity, nowDatetime,))
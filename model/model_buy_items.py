import sqlite3
from model.model_check_DB import *

def exec_buy_items(buy_item_id, buy_item_quntity):
    
    itemData =[]

    item_data = dict(c.execute('SELECT items WHERE id = ?', (buy_item_id)))
    
    c.execute('UPDATE items SET quantity = ? WHERE id =?', (itemData[3]-buy_item_quntity , buy_item_id))
    conn.commit
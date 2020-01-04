import sqlite3
import datetime

now = datetime.datetime.now()
conn = sqlite3.connect('./resource/mudDB.db', isolation_level=None)

nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S')
c = conn.cursor()

# 테이블 생성 및 체크

def check_DB():
    c.execute("CREATE TABLE IF NOT EXISTS items(id INTEGER PRIMARY KEY, item_name TEXT,\
    item_price INTEGER, item_quantity INTEGER, regdate TEXT )")


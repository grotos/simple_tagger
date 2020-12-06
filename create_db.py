import sqlite3

db_loc = "acler.db"

with open("db_init.sql","r", encoding="utf-8") as in_file:
    sql_stmt = in_file.read().splitlines()

conn = sqlite3.connect(db_loc)
cursor = conn.cursor()

for item in sql_stmt:
    cursor.execute(item)

conn.commit()
conn.close()
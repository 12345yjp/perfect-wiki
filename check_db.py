import sqlite3

conn = sqlite3.connect("D:/perfect-wiki/perfect-wiki.db")
curs = conn.cursor()
curs.execute("SELECT name, data FROM other")
for r in curs.fetchall():
    print(f"{r[0]}: {r[1][:80] if r[1] else ''}")
conn.close()

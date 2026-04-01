import sqlite3

conn = sqlite3.connect("D:/perfect-wiki/perfect-wiki.db")
curs = conn.cursor()

# name 필드가 있는지 확인
curs.execute("SELECT name FROM other WHERE name = 'name'")
result = curs.fetchone()
print(f"name exists: {result}")

# 모든 other 테이블 데이터 확인
curs.execute("SELECT * FROM other")
print("\nAll other table data:")
for r in curs.fetchall():
    print(f"  {r}")

conn.close()

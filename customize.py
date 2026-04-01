import sqlite3

conn = sqlite3.connect("D:/perfect-wiki/perfect-wiki.db")
curs = conn.cursor()

# 위키 이름 변경
curs.execute("UPDATE other SET data = ? WHERE name = ?", ["Perfect Wiki", "name"])

# 프론트페이지 설정
curs.execute("SELECT data FROM other WHERE name = ?", ["frontpage"])
if not curs.fetchone():
    curs.execute(
        'INSERT INTO other (name, data, coverage) VALUES (?, ?, "")',
        ["frontpage", "FrontPage"],
    )
else:
    curs.execute("UPDATE other SET data = ? WHERE name = ?", ["FrontPage", "frontpage"])

conn.commit()
conn.close()
print("Done! Wiki name: Perfect Wiki, FrontPage: FrontPage")

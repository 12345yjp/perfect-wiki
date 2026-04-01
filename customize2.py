import sqlite3

conn = sqlite3.connect("D:/perfect-wiki/perfect-wiki.db")
curs = conn.cursor()

# 위키 이름 추가
curs.execute(
    "INSERT INTO other (coverage, name, data) VALUES ('', 'name', 'Perfect Wiki')"
)

# frontpage가 비어있을 경우 기본값 설정
curs.execute("SELECT data FROM other WHERE name = 'frontpage'")
result = curs.fetchone()
if not result or result[0] == "":
    curs.execute("UPDATE other SET data = 'FrontPage' WHERE name = 'frontpage'")

conn.commit()
conn.close()
print("Done! Wiki name set to 'Perfect Wiki'")

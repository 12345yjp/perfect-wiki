# Perfect Wiki 초기화 및 커스터마이징 스크립트

import sqlite3
import os
import sys


def init_wiki_settings():
    db_file = "perfect-wiki.db"

    if not os.path.exists(db_file):
        print(f"Database {db_file} not found. Please run the wiki first.")
        return

    conn = sqlite3.connect(db_file)
    curs = conn.cursor()

    # 위키 이름 설정
    settings = [
        ("name", "Perfect Wiki"),
        (
            "body",
            """
<div style="text-align: center; margin-bottom: 20px;">
    <h1>Welcome to Perfect Wiki!</h1>
    <p>오픈나무 기반의 나만의 위키입니다.</p>
</div>
""",
        ),
    ]

    for name, data in settings:
        try:
            # 기존 값 확인
            curs.execute("SELECT data FROM other WHERE name = ?", [name])
            result = curs.fetchone()

            if result:
                curs.execute("UPDATE other SET data = ? WHERE name = ?", [data, name])
            else:
                curs.execute(
                    'INSERT INTO other (name, data, coverage) VALUES (?, ?, "")',
                    [name, data],
                )
        except Exception as e:
            print(f"Error setting {name}: {e}")

    conn.commit()
    conn.close()
    print("Wiki settings updated!")


if __name__ == "__main__":
    init_wiki_settings()

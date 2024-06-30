import sqlite3
from flask import g, current_app

def get_db(database_name):
    if database_name not in g:
        g.database_name = sqlite3.connect(database_name)
    return g.database_name

def init_db(app, database_name, schema_filename):
    db = get_db(database_name)
    with app.open_resource(schema_filename, mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()

def close_connection(exception):
    databases = ['userDB.db', 'placeDB.db']
    for db_name in databases:
        db = getattr(g, db_name, None)
        if db is not None:
            db.close()


def make_example():
    # 데이터베이스 파일 연결 (없으면 생성)
    conn = sqlite3.connect("placeDB.db")
    # 커서 생성
    c = conn.cursor()
    # 테이블 생성
    try:
        # 샘플 데이터 삽입
        c.execute("INSERT INTO place (pid, pAddrs, pinfo, pXY, pTime) VALUES ('KAK001', '서울시 강남구', 'PSY GangnamStyle', '37.4979,127.0276', '2024-06-30 12:00:00')")
        c.execute("INSERT INTO place (pid, pAddrs, pinfo, pXY, pTime) VALUES ('KAK002', '부산시 해운대구', 'Beautiful Beach', '35.1587,129.1604', '2024-06-30 14:00:00')")
        c.execute("INSERT INTO place (pid, pAddrs, pinfo, pXY, pTime) VALUES ('KAK003', '대구시 북구', 'Historic Sites', '35.8857,128.6226', '2024-06-30 16:00:00')")
        print("Table Made")
    except:
        pass
    # 변경사항 저장 및 연결 종료
    conn.commit()
    conn.close()

make_example()
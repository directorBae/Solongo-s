-- schema.sql

-- 사용자 정보를 저장할 테이블
CREATE TABLE IF NOT EXISTS user (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    uid TEXT NOT NULL UNIQUE,
    upw TEXT NOT NULL,
    nickname TEXT NOT NULL,
    country TEXT
);

-- 장소 정보를 저장할 테이블
CREATE TABLE IF NOT EXISTS place (
    pid TEXT PRIMARY KEY,
    pAddrs TEXT,
    pinfo TEXT,
    pXY TEXT,
    pTime TEXT
);
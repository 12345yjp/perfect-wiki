@echo off
REM Perfect Wiki 실행 스크립트 (Windows)

set NAMU_DB_TYPE=mysql
set NAMU_DB=perfect_wiki
set NAMU_DB_HOST=127.0.0.1
set NAMU_DB_PORT=3306
set NAMU_DB_USER=root
set NAMU_DB_PASSWORD=perfectwiki
set NAMU_HOST=0.0.0.0
set NAMU_PORT=3000
set NAMU_GOLANGPORT=3001
set NAMU_LANG=ko-KR
set NAMU_MARKUP=namumark
set NAMU_ENCRYPT=sha3

python app.py
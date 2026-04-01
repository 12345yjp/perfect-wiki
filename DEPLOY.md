# Perfect Wiki - Render 배포 설정

## 방법

### 1. GitHub에 푸시
```bash
cd D:/perfect-wiki
git add .
git commit -m "Add perfect-wiki with Liberty skin"
git remote add origin https://github.com/사용자명/perfect-wiki.git
git push -u origin main
```

### 2. Render에서 배포
1. https://render.com 접속
2. "New" > "Web Service" 선택
3. GitHub 저장소 연결
4. 설정:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `python app.py`
   - Environment Variables:
     - `NAMU_DB_TYPE`: `mysql`
     - `NAMU_DB`: `perfect_wiki`
     - `NAMU_DB_HOST`: `${DB_HOST}`
     - `NAMU_DB_PORT`: `3306`
     - `NAMU_DB_USER`: `root`
     - `NAMU_DB_PASSWORD`: `${DB_PASSWORD}`
     - `NAMU_HOST`: `0.0.0.0`
     - `NAMU_PORT`: `3000`
     - `NAMU_GOLANGPORT`: `3001`
     - `NAMU_LANG`: `ko-KR`
     - `NAMU_MARKUP`: `namumark`
     - `NAMU_ENCRYPT`: `sha3`

### 3. PostgreSQL 추가
- Render 웹서비스 생성 후 "New" > "PostgreSQL" 선택
- 생성된 DB 정보를 환경변수에 설정

## 접속
- 로컬: http://localhost:3000
- 배포: Render에서 생성된 URL

## 스킨 변경
- 관리자 로그인 후 /skin_set 에서 Liberty 스킨 선택
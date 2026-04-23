# Tubelens Clone

AI 기반 떡상 영상 탐지 및 유튜브 성장 분석 플랫폼.

## 주요 기능

- 급상승 가능 영상 스코어링
- CTR 추정
- Velocity 기반 떡상 점수
- 니치 키워드 탐지
- 경쟁강도 분석

## Stack

Frontend:
- Next.js
- TypeScript
- Tailwind

Backend:
- FastAPI
- Python
- PostgreSQL
- Redis (optional)

---

## 설치

git clone https://github.com/yourname/tubelens-clone.git 
cd tubelens-clone

### Frontend
cd frontend
npm install
npm run dev

### Backend
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload

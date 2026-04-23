# # Tubelens 스타일 프로젝트 (GitHub 업로드용 완성 패키지)

## 추천 레포 구조

```text
tubelens-clone/
├── frontend/                 # Next.js
│   ├── app/
│   │   ├── page.tsx
│   │   ├── dashboard/page.tsx
│   │   └── api/
│   ├── components/
│   │   ├── TrendTable.tsx
│   │   └── ScoreCard.tsx
│   ├── lib/
│   │   └── api.ts
│   ├── package.json
│   ├── next.config.js
│   └── .env.example
│
├── backend/                  # FastAPI
│   ├── app/
│   │   ├── main.py
│   │   ├── routes/
│   │   │   └── videos.py
│   │   ├── services/
│   │   │   ├── trend_detector.py
│   │   │   └── youtube_collector.py
│   │   └── models/
│   ├── requirements.txt
│   └── .env.example
│
├── docker-compose.yml
├── README.md
└── .gitignore
```

---

# README.md

```md
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

```

---

# backend/app/main.py

```python
from fastapi import FastAPI
from app.routes.videos import router

app = FastAPI(title='Tubelens Clone')

app.include_router(router)
```

---

# backend/app/routes/videos.py

```python
from fastapi import APIRouter
from app.services.trend_detector import detect_trending

router = APIRouter()

@router.get('/trending')
def trending():
    return detect_trending()
```

---

# backend/app/services/trend_detector.py

```python
import math

def virality_score(video):

    velocity=(video['views_24h']/max(video['subs'],1))*100

    ctr_score=video['ctr']*20

    retention=video['retention']*15

    competition=(1/video['competition'])*20

    novelty=video['keyword_gap']*15

    growth=math.log(video['views_growth']+1)*10

    score=(
      velocity+
      ctr_score+
      retention+
      competition+
      novelty+
      growth
    )

    return round(score,2)


def detect_trending():

    samples=[
      {
      'title':'AI Shorts Automation',
      'views_24h':83000,
      'subs':12000,
      'ctr':7.8,
      'retention':0.64,
      'competition':0.25,
      'keyword_gap':0.91,
      'views_growth':310
      },
      {
      'title':'Faceless Finance Channel',
      'views_24h':51000,
      'subs':18000,
      'ctr':6.9,
      'retention':0.60,
      'competition':0.33,
      'keyword_gap':0.80,
      'views_growth':240
      }
    ]

    for v in samples:
        v['trend_score']=virality_score(v)

    return sorted(samples,key=lambda x:x['trend_score'],reverse=True)
```

---

# frontend/app/page.tsx

```tsx
async function getData(){
 const res=await fetch('http://localhost:8000/trending')
 return res.json()
}

export default async function Home(){
 const videos=await getData()

 return(
<div className='p-10'>
<h1 className='text-4xl font-bold mb-8'>TUBELENS SIGNALS</h1>

{videos.map((v:any)=>(
<div
key={v.title}
className='border rounded-xl p-6 mb-6 shadow'
>
<h2 className='text-2xl font-bold'>
{v.title}
</h2>

<p>Trend Score: {v.trend_score}</p>
<p>CTR: {v.ctr}%</p>
<p>Retention: {v.retention}</p>

</div>
))}

</div>
)
}
```

---

# requirements.txt

```txt
fastapi
uvicorn
python-dotenv
pydantic
requests
pandas
numpy
```

---

# package.json

```json
{
"name":"tubelens-clone",
"private":true,
"scripts":{
"dev":"next dev",
"build":"next build"
},
"dependencies":{
"next":"latest",
"react":"latest",
"react-dom":"latest"
}
}
```

---

# docker-compose.yml

```yaml
version: '3'

services:
 frontend:
   build: ./frontend
   ports:
    - "3000:3000"

 backend:
   build: ./backend
   ports:
    - "8000:8000"
```

---

# .gitignore

```bash
node_modules/
__pycache__/
.env
.next/
venv/
*.pyc
```

---

## GitHub 업로드

```bash
git init
git add .
git commit -m "Initial Tubelens Clone"
git branch -M main
git remote add origin https://github.com/USERNAME/tubelens-clone.git
git push -u origin main
```

---

## 다음 단계(실제 Tubelens 수준 업그레이드)

추가하면 거의 SaaS 수준 됨:

### 1. YouTube Data API 수집

* 실시간 조회수 속도 추적
* 구독자 대비 비정상 성장 탐지

### 2. 떡상 예측 모델

추가 피처:

```python
thumbnail_emotion_score
comment_velocity
search_volume_gap
trend_decay_ratio
```

LightGBM/XGBoost로 예측 가능.

---

## 수익화 가능 기능

* 월 구독형 대시보드
* 떡상 키워드 알림
* 채널 진단 리포트
* 쇼츠 자동 발굴 SaaS

---

원하면 다음 단계로 "Tubelens 실제 알고리즘 고도화(ML 점수모델 + 유튜브 API 연결)"도 이어서 확장 가능.

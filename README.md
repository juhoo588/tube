# Tubelens 스타일 프로젝트 (GitHub 업로드용 완성 패키지)

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

---

# 확장 1 — ML 기반 떡상 예측 엔진

## feature_engineering.py

```python
import pandas as pd

def make_features(video):
    return {
      'velocity_ratio': video['views_24h']/max(video['subs'],1),
      'ctr': video['ctr'],
      'retention': video['retention'],
      'comment_velocity': video['comments_1h'],
      'keyword_gap': video['keyword_gap'],
      'competition': video['competition'],
      'thumbnail_emotion_score': video['thumbnail_score']
    }
```

## train_model.py

```python
from lightgbm import LGBMClassifier

X_train=training_features
y_train=viral_labels

model=LGBMClassifier(
 n_estimators=500,
 learning_rate=0.03,
 max_depth=7
)

model.fit(X_train,y_train)
```

예측 결과:

```python
viral_probability=model.predict_proba([features])[0][1]
```

0.85 이상이면 떡상 후보.

---

# 확장 2 — YouTube Data API 수집기

## youtube_collector.py

```python
from googleapiclient.discovery import build

youtube=build(
 'youtube',
 'v3',
 developerKey=API_KEY
)

def search_niche(keyword):

 req=youtube.search().list(
   part='snippet',
   q=keyword,
   order='date',
   maxResults=20
 )

 return req.execute()
```

탐지 로직:

* 최근 업로드 영상만 추출
* 24시간 조회속도 계산
* 구독자 대비 비정상 성장 감지

---

# 확장 3 — 썸네일 CTR 분석기

```python
def thumbnail_ctr_score(
 emotion,
 contrast,
 text_density,
 curiosity_gap
):

 return (
   emotion*0.35+
   contrast*0.2+
   curiosity_gap*0.35-
   text_density*0.1
 )
```

향후 CV 모델:

* YOLO
* CLIP
* Vision Transformer

---

# 확장 4 — 키워드 갭 탐지기

```python
def keyword_gap(search_volume,video_count):
 return search_volume/(video_count+1)
```

높은 값 = 블루오션 니치.

예:

* faceless ai tools
* ai news shorts
* finance automation

---

# 확장 5 — DB 스키마

```sql
videos(
 id,
 title,
 channel,
 velocity,
 ctr,
 retention,
 trend_score,
 viral_probability,
 created_at
)
```

```sql
keyword_signals(
 keyword,
 gap_score,
 competition,
 search_volume
)
```

---

# 확장 6 — Tubelens식 Opportunity Score

```python
def opportunity_score(
 demand,
 low_comp,
 growth,
 monetization
):
 return (
 demand*.3+
 low_comp*.3+
 growth*.25+
 monetization*.15
 )
```

100점 스케일로 랭킹.

---

# 추천 추가 SaaS 기능

* Rising Before Viral 알림봇
* Shorts Hunter 스캐너
* Competitor Gap Finder
* Thumbnail A/B predictor
* 제목 생성기(CTR optimizer)

---

## 향후 배포 구조

```text
Next.js → Vercel
FastAPI → Railway
Postgres → Supabase
Redis → Upstash
Workers → Celery
```

---

---

# 확장 7 — Shorts 자동 발굴 봇

## 발굴 로직 핵심 지표

초기 6~24시간 데이터 기준:

```python
def shorts_signal(video):

 velocity=(video['views_6h']/video['subs'])
 engagement=(video['likes']+video['comments'])/video['views']
 retention=video['avg_view_percent']

 score=(
 velocity*0.4+
 engagement*0.3+
 retention*0.3
 )

 return score
```

---

## rising_shorts_bot.py

```python
from youtube_collector import search_niche

WATCH_KEYWORDS=[
 'ai tools',
 'crypto news',
 'side hustle',
 'faceless shorts'
]

def hunt_rising_shorts():

 winners=[]

 for kw in WATCH_KEYWORDS:
   videos=search_niche(kw)

   for v in videos:
      signal=shorts_signal(v)

      if signal>0.82:
         winners.append(v)

 return sorted(
   winners,
   key=lambda x:x['views_6h'],
   reverse=True
 )
```

---

## 알림봇 (급상승 포착)

```python
if signal > 0.90:
 send_discord_alert(video)
```

Slack/Discord/Telegram 연동 가능.

---

# 확장 8 — 경쟁 채널 역공학 분석 엔진

경쟁 채널별 성공패턴 추출.

## competitor_reverse_engine.py

```python
def channel_pattern(channel):

 return {
  'avg_title_length':42,
  'hook_style':'curiosity',
  'thumbnail_emotion':'shock',
  'avg_post_freq':2.1,
  'winning_topics':[
      'AI automation',
      'finance hacks'
   ]
 }
```

---

## 경쟁 채널 복제 가능 패턴 추출

```python
def opportunity_gap(my_channel,competitor):

 gaps=[]

 for topic in competitor['winning_topics']:
   if topic not in my_channel['covered_topics']:
      gaps.append(topic)

 return gaps
```

결과:

* 경쟁채널 잘 먹히는 포맷
* 아직 내가 안 다룬 블루오션 주제
* 썸네일/제목 패턴 복원

---

## 제목 역공학

```python
Top titles:

I Made $1000 Using AI in 7 Days
This Faceless Channel Grew To 1M Views
3 AI Tools Nobody Is Using Yet
```

공통패턴:

Formula:
[Number] + Curiosity + Underserved Topic

````

---

## Shorts 포맷 역공학

분석 지표:

```python
hook_first_3_seconds
caption_density
cut_frequency
subtitle_velocity
loopability_score
````

loopability 높으면 쇼츠 폭발 가능성 큼.

---

# 경쟁채널 스파이 대시보드 구조

```sql
competitor_channels(
 channel,
 viral_ratio,
 avg_ctr,
 avg_retention
)
```

```sql
viral_patterns(
 topic,
 hook_type,
 thumbnail_type,
 views_multiplier
)
```

---

## 완성형 SaaS 구조 (Tubelens급)

모듈 4개:

1. Trend Hunter
2. Shorts Hunter Bot
3. Competitor Reverse Engine
4. Viral Predictor

월 구독화 가능.

---

## 다음 고도화 가능

원하면 다음엔 실제 Tubelens 수준으로

* 경쟁 채널 역공학 분석
* 떡상 영상 조기 감지(24시간 이내)
* Shorts 자동 발굴 봇
* 구독형 SaaS 과금 구조
  까지 확장 가능.

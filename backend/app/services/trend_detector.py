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

from app.services.youtube_collector import search_niche

WATCH_KEYWORDS=[
 'ai tools',
 'crypto news',
 'side hustle',
 'faceless shorts'
]

def shorts_signal(video):
    velocity = video['views_6h'] / video['subs']
    engagement = (video['likes'] + video['comments']) / video['views']
    retention = video['avg_view_percent']

    score = (
        velocity * 0.4 +
        engagement * 0.3 +
        retention * 0.3
    )
    return score

def hunt_rising_shorts():
    winners = []
    for kw in WATCH_KEYWORDS:
        videos = search_niche(kw)
        for v in videos:
            signal = shorts_signal(v)
            if signal > 0.82:
                winners.append(v)

    return sorted(winners, key=lambda x: x['views_6h'], reverse=True)

def channel_pattern(channel):
    return {
      'avg_title_length': 42,
      'hook_style': 'curiosity',
      'thumbnail_emotion': 'shock',
      'avg_post_freq': 2.1,
      'winning_topics': [
          'AI automation',
          'finance hacks'
       ]
    }

def opportunity_gap(my_channel, competitor):
    gaps = []
    for topic in competitor['winning_topics']:
        if topic not in my_channel.get('covered_topics', []):
            gaps.append(topic)
    return gaps

def thumbnail_ctr_score(emotion, contrast, text_density, curiosity_gap):
    return (
       emotion * 0.35 +
       contrast * 0.2 +
       curiosity_gap * 0.35 -
       text_density * 0.1
    )

def keyword_gap(search_volume, video_count):
    return search_volume / (video_count + 1)

def opportunity_score(demand, low_comp, growth, monetization):
    return (
        demand * 0.3 +
        low_comp * 0.3 +
        growth * 0.25 +
        monetization * 0.15
    )

def shorts_signal(video):
    velocity = video['views_6h'] / video['subs']
    engagement = (video['likes'] + video['comments']) / video['views']
    retention = video['avg_view_percent']
    score = velocity * 0.4 + engagement * 0.3 + retention * 0.3
    return score

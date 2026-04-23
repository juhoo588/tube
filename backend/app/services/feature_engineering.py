import pandas as pd

def make_features(video):
    return {
      'velocity_ratio': video['views_24h']/max(video['subs'],1),
      'ctr': video['ctr'],
      'retention': video['retention'],
      'comment_velocity': video.get('comments_1h', 0),
      'keyword_gap': video['keyword_gap'],
      'competition': video['competition'],
      'thumbnail_emotion_score': video.get('thumbnail_score', 0)
    }

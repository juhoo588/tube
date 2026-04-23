from googleapiclient.discovery import build

# YouTube Data API 수집기
# TODO: API 키 설정 후 구현

def search_niche(keyword, api_key):
    youtube = build('youtube', 'v3', developerKey=api_key)

    req = youtube.search().list(
        part='snippet',
        q=keyword,
        order='date',
        maxResults=20
    )

    return req.execute()

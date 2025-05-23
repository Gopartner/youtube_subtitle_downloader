import re
from youtube_transcript_api import YouTubeTranscriptApi

def get_video_id(url):
    patterns = [
        r'(?:https?:\/\/)?(?:www\.)?youtube\.com\/watch\?v=([^&]+)',
        r'(?:https?:\/\/)?(?:www\.)?youtu\.be\/([^?]+)',
        r'(?:https?:\/\/)?(?:www\.)?youtube\.com\/embed\/([^\/]+)',
        r'(?:https?:\/\/)?(?:www\.)?youtube\.com\/v\/([^\/]+)'
    ]
    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)
    return url.strip()

def get_available_languages(video_id):
    try:
        transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)
        langs = []
        for t in transcript_list:
            label = "manual" if not t.is_generated else "auto-generated"
            langs.append(f"{t.language_code} ({label})")
        return langs
    except Exception as e:
        print(f"❌ Gagal mendapatkan bahasa: {e}")
        return None


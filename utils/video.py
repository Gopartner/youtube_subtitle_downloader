# utils/video.py

import re
import requests
from youtube_transcript_api import YouTubeTranscriptApi

def get_video_id(url):
    url = url.strip()
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
    return url

def get_available_languages(video_id):
    try:
        transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)
        langs = []
        for t in transcript_list:
            label = "manual" if not t.is_generated else "auto-generated"
            langs.append(f"{t.language_code} ({label})")
        return sorted(langs)
    except Exception as e:
        print(f"❌ Gagal mendapatkan bahasa: {e}")
        return None

def get_video_title(video_id):
    try:
        url = f"https://www.youtube.com/watch?v={video_id}"
        response = requests.get(url, timeout=5)
        match = re.search(r'<title>(.*?)</title>', response.text)
        if match:
            title = match.group(1).replace("- YouTube", "").strip()
            return title
        return "unknown_title"
    except Exception as e:
        print(f"❌ Gagal mengambil judul video: {e}")
        return "unknown_title"


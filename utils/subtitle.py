import os
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter
from .video import get_available_languages, get_video_title

def get_subtitles(video_id, language='id', output_file=None):
    try:
        transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)

        try:
            transcript = transcript_list.find_transcript([language]).fetch()
        except:
            print(f"⚠️ Subtitle '{language}' tidak ditemukan. Mencoba versi otomatis...")
            generated = [t for t in transcript_list if t.is_generated]
            if generated:
                transcript = generated[0].fetch()

                if not transcript or len(transcript) == 0:
                    raise Exception("Subtitle otomatis kosong. YouTube mungkin membatasi akses subtitle video ini.")
            else:
                raise Exception("Tidak ada subtitle sama sekali.")

        # Cek ulang isi transcript sebelum diformat
        if not transcript or len(transcript) == 0:
            raise Exception("Subtitle ditemukan tapi kosong.")

        text = TextFormatter().format_transcript(transcript)

        if output_file is None:
            title = get_video_title(video_id)
            output_file = f"{title.lower().replace(' ', '_')}_{language}.txt"

        os.makedirs("results", exist_ok=True)
        output_path = os.path.join("results", output_file)

        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(text)

        print(f"💾 Subtitle disimpan ke '{output_path}'")
        return True

    except Exception as e:
        print(f"❌ Error: {e}")
        langs = get_available_languages(video_id)
        if langs:
            print("\nSubtitle tersedia:")
            for lang in langs:
                print(f"- {lang}")
        else:
            print("Tidak ada subtitle yang tersedia")
        return False


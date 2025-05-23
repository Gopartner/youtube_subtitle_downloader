import os
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter
from .video import get_available_languages

def get_subtitles(video_id, language='id', output_file=None):
    try:
        transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)

        # Coba ambil subtitle sesuai permintaan
        try:
            transcript = transcript_list.find_transcript([language]).fetch()
        except:
            print(f"⚠️ Subtitle '{language}' tidak ditemukan. Mencoba versi otomatis...")
            generated = [t for t in transcript_list if t.is_generated]
            if generated:
                transcript = generated[0].fetch()
                if not transcript:
                    raise Exception("Subtitle otomatis gagal diambil. Mungkin dibatasi oleh YouTube.")
            else:
                raise Exception("Tidak ada subtitle sama sekali.")

        # Format subtitle ke teks biasa
        text = TextFormatter().format_transcript(transcript)

        # Simpan ke file jika diminta
        if output_file:
            if not output_file.endswith(".txt"):
                output_file += ".txt"

            # Buat folder `results/` jika belum ada
            os.makedirs("results", exist_ok=True)

            output_path = os.path.join("results", output_file)

            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(text)

            print(f"💾 Subtitle disimpan ke '{output_path}'")
        else:
            print("\n=== HASIL SUBTITLE ===\n")
            print(text)

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


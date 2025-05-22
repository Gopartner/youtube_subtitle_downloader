from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter
import re

def get_video_id(url):
    """
    Ekstrak ID video dari URL YouTube
    """
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
    """
    Dapatkan daftar bahasa subtitle yang tersedia
    """
    try:
        transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)
        available_langs = []
        
        # Subtitle buatan manusia
        for transcript in transcript_list:
            if not transcript.is_generated:
                available_langs.append(f"{transcript.language_code} (manual)")
        
        # Subtitle otomatis
        for transcript in transcript_list:
            if transcript.is_generated:
                available_langs.append(f"{transcript.language_code} (auto-generated)")
        
        return available_langs
    except Exception as e:
        print(f"Error saat memeriksa bahasa yang tersedia: {e}")
        return None

def get_subtitles(video_id, language='id', output_file=None):
    """
    Ambil subtitle dari video YouTube
    """
    try:
        # Cek subtitle yang tersedia
        transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)
        
        # Coba ambil subtitle dengan bahasa yang diminta
        try:
            transcript = transcript_list.find_transcript([language]).fetch()
        except:
            # Jika tidak ada, coba ambil subtitle otomatis
            print(f"\nSubtitle dalam bahasa '{language}' tidak tersedia, mencoba mengambil subtitle otomatis...")
            generated_transcripts = [t for t in transcript_list if t.is_generated]
            if generated_transcripts:
                transcript = generated_transcripts[0].fetch()
            else:
                raise Exception("Tidak ada subtitle yang tersedia")
        
        # Format teks
        formatter = TextFormatter()
        text = formatter.format_transcript(transcript)

        # Output ke file atau print ke console
        if output_file:
            if not output_file.endswith('.txt'):
                output_file += '.txt'
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(text)
            print(f"\nSubtitle berhasil disimpan ke '{output_file}'")
        else:
            print("\n=== HASIL SUBTITLE ===\n")
            print(text)
        
        return True
        
    except Exception as e:
        print(f"\nError: {e}")
        available_langs = get_available_languages(video_id)
        if available_langs:
            print("\nSubtitle tersedia dalam bahasa berikut:")
            for lang in available_langs:
                print(f"- {lang}")
        else:
            print("Video ini tidak memiliki subtitle yang tersedia")
        return False

def main():
    print("\n=== YouTube Subtitle Downloader ===")
    print("Script untuk mengambil subtitle dari video YouTube\n")
    
    while True:
        # Input URL dari pengguna
        url = input("\nMasukkan URL YouTube atau ID video (ketik 'exit' untuk keluar): ").strip()
        
        if url.lower() == 'exit':
            print("\nTerima kasih telah menggunakan program ini!")
            break
        
        if not url:
            print("\nHarap masukkan URL atau ID video!")
            continue
        
        # Ekstrak ID video
        video_id = get_video_id(url)
        print(f"\nMencari subtitle untuk video ID: {video_id}")
        
        # Tampilkan bahasa yang tersedia
        available_langs = get_available_languages(video_id)
        if available_langs:
            print("\nSubtitle tersedia dalam bahasa berikut:")
            for lang in available_langs:
                print(f"- {lang}")
        
        # Input bahasa
        language = input("\nMasukkan kode bahasa (contoh: 'id' untuk Indonesia, kosongkan untuk default): ").strip() or 'id'
        
        # Tanya apakah ingin menyimpan ke file
        save_to_file = input("\nSimpan ke file? (y/n): ").strip().lower() == 'y'
        output_file = None
        
        if save_to_file:
            output_file = input("\nMasukkan nama file output (contoh: subtitle.txt): ").strip()
            if not output_file:
                output_file = f"youtube_subtitle_{video_id}.txt"
        
        # Proses pengambilan subtitle
        print("\nMemproses...")
        success = get_subtitles(video_id, language, output_file)
        
        if success:
            # Tanya apakah ingin melanjutkan
            continue_search = input("\nApakah Anda ingin mencari subtitle lagi? (y/n): ").strip().lower()
            if continue_search != 'y':
                print("\nTerima kasih telah menggunakan program ini!")
                break

if __name__ == "__main__":
    main()

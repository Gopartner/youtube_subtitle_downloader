from utils.video import get_video_id, get_available_languages
from utils.subtitle import get_subtitles
from utils.feedback import info, success, warning

def main():
    print("\n=== YouTube Subtitle Downloader ===")
    print("Script untuk mengambil subtitle dari video YouTube\n")

    while True:
        url = input("\nMasukkan URL YouTube atau ID video (ketik 'exit' untuk keluar): ").strip()
        if url.lower() == 'exit':
            print("\n👋 Terima kasih telah menggunakan program ini!")
            break
        if not url:
            warning("Harap masukkan URL atau ID video!")
            continue

        info("Mengekstrak ID dari URL...")
        video_id = get_video_id(url)
        print(f"📽️ Video ID: {video_id}")

        info("Mengambil daftar subtitle...")
        available_langs = get_available_languages(video_id)
        if available_langs:
            print("🌐 Subtitle tersedia:")
            for lang in available_langs:
                print(f"- {lang}")
        else:
            warning("Tidak ada subtitle yang tersedia")
            continue

        language = input("\nMasukkan kode bahasa (contoh: 'id', 'en'): ").strip() or 'id'
        save_to_file = input("Simpan ke file? (y/n): ").strip().lower() == 'y'
        output_file = None

        if save_to_file:
            output_file = input("Masukkan nama file output: ").strip()
            if not output_file:
                output_file = f"subtitle_{video_id}.txt"

        info("Mengambil subtitle...")
        success_flag = get_subtitles(video_id, language, output_file)

        if success_flag:
            success("Selesai mengambil subtitle!")

        lanjut = input("\nIngin cari subtitle lain? (y/n): ").strip().lower()
        if lanjut != 'y':
            print("\n👋 Terima kasih telah menggunakan program ini!")
            break

if __name__ == "__main__":
    main()


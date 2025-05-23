# 🎬 YouTube Subtitle Downloader

Alat CLI Python untuk mengambil subtitle (manual dan otomatis) dari video YouTube. Mendukung pemilihan bahasa, penyimpanan ke file `.txt`, dan pencarian subtitle otomatis jika bahasa tidak tersedia.

---

## 🛠️ Fitur

- Ambil subtitle dari YouTube (manual dan auto-generated)
- Pilih bahasa subtitle (`id`, `en`, dll)
- Simpan hasil ke file `.txt`
- Support berbagai format URL YouTube (link biasa, shortlink, embed, dll)
- Modular dan mudah dikembangkan

---

## 📦 Instalasi

### 1. Clone repositori
```bash
git clone https://github.com/Gopartner/youtube_subtitle_downloader.git
cd youtube-subtitle-downloader
```
## struktur project
```bash
youtube-subtitle-downloader/
├── README.md                 # Dokumentasi penggunaan project
├── main.py                   # Entry point program (interaktif)
├── requirements.txt          # Daftar dependensi Python
├── .gitignore                # Mengatur file/folder yang diabaikan Git
├── results/                  # Folder hasil subtitle (output)
│   └── .gitkeep              # Placeholder agar folder tetap muncul di Git
└── utils/                    # Folder berisi modul bantu (modular)
    ├── __init__.py           # Penanda folder Python package
    ├── feedback.py           # Indikator proses (spinner/loading)
    ├── subtitle.py           # Fungsi ambil & simpan subtitle
    └── video.py              # Fungsi bantu: parsing URL & bahasa

```

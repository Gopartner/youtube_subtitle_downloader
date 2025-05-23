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
│
├── main.py                      # Entry point CLI
├── requirements.txt             # Dependensi
├── README.md                    # Dokumentasi
│
├── utils/                       # Folder modul utama
│   ├── __init__.py
│   ├── video.py                 # Fungsi ekstrak ID & bahasa subtitle
│   ├── subtitle.py              # Fungsi ambil & simpan subtitle
│   └── feedback.py              # Tampilan progress/indikator

```

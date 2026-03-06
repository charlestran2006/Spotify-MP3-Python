# 🎵 SpotifyLocalPrep

A Python desktop app that prepares your **legally owned** music files for [Spotify Local Files](https://support.spotify.com/us/article/local-files/) — converting, tagging, and organizing them into a clean folder structure so Spotify can find and play them.

> **Note:** This tool only works with audio files you already own or have the rights to use. It does not download music from any source.

---

## Features

- 📂 **Scan** a folder for supported audio files (MP3, FLAC, WAV, M4A, AAC, OGG)
- 🔄 **Convert** non-MP3 files to MP3 using ffmpeg (320kbps)
- ✏️ **Edit metadata** — title, artist, album, track number, genre, year
- 🖼 **Embed album art** from any local image file
- 📁 **Organize** output into `Artist/Album/01 - Title.mp3` structure
- 👁 **Preview** all changes before anything is written to disk
- ⚠️ **Detect duplicates** by title+artist or conflicting output paths
- 📋 **Live log panel** with color-coded status messages
- ✅ **Skip or replace** on output file conflicts — your choice

---

## Requirements

| Requirement | Version |
|-------------|---------|
| Python | 3.10 or newer |
| ffmpeg | Any recent version |
| OS | Windows 10/11 (macOS/Linux should also work) |

---

## Quick Start

### 1. Install ffmpeg

**Windows (recommended):**
```powershell
winget install ffmpeg
```

Or download manually from [gyan.dev/ffmpeg/builds](https://www.gyan.dev/ffmpeg/builds/), extract to `C:\ffmpeg`, and add `C:\ffmpeg\bin` to your system PATH.

Verify:
```
ffmpeg -version
```

**macOS:**
```bash
brew install ffmpeg
```

**Linux:**
```bash
sudo apt install ffmpeg
```

---

### 2. Clone the repo

```bash
git clone https://github.com/YOUR_USERNAME/spotify-local-prep.git
cd spotify-local-prep
```

---

### 3. Create a virtual environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate.bat

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

---

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 5. Run the app

```bash
python main.py
```

---

## How to Use

1. **Select Input Folder** — Browse to the folder containing your music files
2. **Select Output Folder** — Choose where processed files should be saved (e.g. a new empty folder called `Spotify_Local_Files_Ready`)
3. **Scan Files** — Click 🔍 Scan Files to find all supported audio in the folder
4. **Edit Metadata** — Click any file in the list to edit its tags; click ✅ Apply Changes to save
5. **Preview** — Click 👁 Preview Changes to review all planned output filenames before anything is written
6. **Export** — Click ▶ Process & Export to convert, tag, and copy everything to the output folder
7. **Add to Spotify** — In Spotify Desktop: `Settings → Local Files → Add a Source` → select your output folder

---

## Output Structure

```
Spotify_Local_Files_Ready/
├── The Beatles/
│   └── Abbey Road/
│       ├── 01 - Come Together.mp3
│       ├── 02 - Something.mp3
│       └── 17 - The End.mp3
├── Pink Floyd/
│   └── The Dark Side of the Moon/
│       └── 01 - Speak to Me.mp3
└── Unknown Artist/
    └── Unknown Album/
        └── untitled_track.mp3
```

---

## Project Structure

```
spotify_local_prep/
├── main.py                     # Entry point
├── requirements.txt
├── README.md
└── app/
    ├── core/
    │   ├── models.py           # AudioFile dataclass
    │   ├── scanner.py          # Folder scanning
    │   ├── converter.py        # ffmpeg conversion
    │   ├── metadata.py         # Tag reading/writing (mutagen)
    │   ├── organizer.py        # Output path builder + sanitizer
    │   ├── duplicates.py       # Duplicate detection
    │   └── exporter.py         # Full pipeline orchestrator
    ├── gui/
    │   ├── main_window.py      # Main window + controller
    │   ├── file_table.py       # Scrollable file list
    │   ├── metadata_panel.py   # Tag editor form
    │   ├── preview_dialog.py   # Before/after preview modal
    │   └── log_panel.py        # Status log widget
    └── utils/
        └── logger.py           # Logging with GUI callback
```

---

## Supported Formats

| Format | Extension | Conversion needed |
|--------|-----------|-------------------|
| MP3 | `.mp3` | No — copied as-is |
| FLAC | `.flac` | Yes → MP3 |
| WAV | `.wav` | Yes → MP3 |
| M4A | `.m4a` | Yes → MP3 |
| AAC | `.aac` | Yes → MP3 |
| OGG Vorbis | `.ogg` | Yes → MP3 |

---

## Dependencies

| Package | Purpose |
|---------|---------|
| [customtkinter](https://github.com/TomSchimansky/CustomTkinter) | Modern dark-mode GUI |
| [mutagen](https://mutagen.readthedocs.io/) | Audio tag reading and writing |
| [Pillow](https://python-pillow.org/) | Album art image loading and preview |
| ffmpeg (system binary) | Audio format conversion |

---

## Roadmap

- [ ] Auto-detect `cover.jpg` / `folder.jpg` as default album art
- [ ] Batch metadata editing (apply to multiple selected files at once)
- [ ] Auto-fetch metadata from MusicBrainz
- [ ] Audio fingerprint deduplication (AcoustID)
- [ ] PyInstaller `.exe` packaging for Windows
- [ ] Drag-and-drop folder import

---

## Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you'd like to change.

1. Fork the repo
2. Create a feature branch: `git checkout -b feature/my-feature`
3. Commit your changes: `git commit -m 'Add my feature'`
4. Push: `git push origin feature/my-feature`
5. Open a Pull Request

---

## License

[MIT](LICENSE)

---

## Legal Notice

This software is intended solely for use with audio files you legally own or have the rights to use. It does not facilitate downloading, ripping from streaming services, bypassing DRM, or accessing copyrighted content without authorization.

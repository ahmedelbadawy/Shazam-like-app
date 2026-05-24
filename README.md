# Shazam-Style Song Recognition

An audio fingerprinting application that identifies a song from a short clip by its spectral signature — a Shazam-style matcher built with **Python** and **PyQt5**. Each song is reduced to a compact perceptual fingerprint, and a query clip is matched against a database to return the closest songs ranked by similarity.

## How It Works

1. **Audio loading** — reads an MP3, takes the first 60 seconds, and converts it to mono WAV.
2. **Feature extraction** — computes two spectral features with librosa: a **mel-spectrogram** and **MFCCs**, each rendered as an image.
3. **Fingerprinting** — converts each feature image into a **perceptual hash** (`phash`), forming a compact, robust fingerprint.
4. **Matching** — compares the query fingerprint against every fingerprint in the database using **Hamming distance**, averages the two feature distances, and maps the result to a **0–100% similarity index**.
5. **Ranking** — returns all songs sorted by similarity, displayed in a results table in the UI.

## Features

- **Single-song identification** — fingerprint one clip and find its closest matches in the database.
- **Two-song mixing** — blend two songs by a user-controlled weighted average (in the time domain), fingerprint the mix, and find what it most resembles. The mixing weight is set with a slider in the UI.
- **Component-aware database** — fingerprints are stored for the full track, the music, and the vocals of each song, and the best-matching component is used for scoring.
- **PyQt5 interface** — browse files, choose the scan mode, run a scan, and view ranked results in a table.

## Tech Stack

| Component        | Technology                         |
|------------------|------------------------------------|
| Language / GUI   | Python, PyQt5                      |
| Audio processing | librosa, pydub, SciPy, NumPy       |
| Fingerprinting   | imagehash (perceptual hashing)     |
| Image handling   | Pillow                             |

## Project Structure

- `main.py` — PyQt5 app: file browsing, scan modes, and the results table.
- `helpers.py` — the `Song` class (audio reading, feature generation, fingerprinting), perceptual hashing, and the fingerprint comparison logic.
- `USER_helpers.py` — two-song weighted-average mixing and fingerprinting.
- `DB_helpers.py` — building and reading the fingerprint database.

## Getting Started

### Prerequisites
- Python 3.x
- FFmpeg installed (required by pydub for MP3 handling)

### Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/ahmedelbadawy/Shazam-like-app
   cd Shazam-like-app
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Build the fingerprint database from your song files (see `DB_helpers.py`).
4. Run the app:
   ```bash
   python main.py
   ```

## Usage
1. Launch the app and browse for one MP3 (single-song mode) or two MP3s (mixing mode).
2. In mixing mode, set the weighting between the two songs with the slider.
3. Press **Scan** to fingerprint the input and match it against the database.
4. View the ranked results, each with a matching percentage, in the table.

## License
[Add your license here]

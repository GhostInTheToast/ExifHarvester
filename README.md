# ExifHarvester

ExifHarvester is a high-performance, local EXIF metadata extraction pipeline built with native Python parallelism. It recursively scans folders of images (including nested folders), extracts metadata from each file, and stores results in a scalable `.jsonl` format.

No cloud services. No Celery. No Redis. Just fast, simple, Python-powered harvesting — ready to scale from hundreds to hundreds of thousands of images.

---

## 🚀 Features

- ✅ Fast parallel processing using `concurrent.futures.ProcessPoolExecutor`
- 📁 Recursively scans nested directories for `.jpg`, `.jpeg`, `.png`
- 🧠 Extracts EXIF metadata using Pillow
- 💾 Saves results as line-by-line JSON (`.jsonl`) for easy streaming
- 🔐 Thread-safe writing using file locks
- 🛑 Ignores large image folders via `.gitignore` (safe for GitHub)

---

## 🧱 Project Structure

```
ExifHarvester/
├── inputImages/             # Drop your folders of images here (can be nested)
├── output/
│   └── metadata.jsonl       # Extracted metadata output (JSON Lines)
├── harvester/
│   ├── imageProcessor.py    # Extracts EXIF metadata using Pillow
│   ├── jsonlWriter.py       # Thread-safe writer to metadata.jsonl
├── main.py                  # Entry point to run the pipeline
├── readExifField.py         # Script to read specific EXIF fields from output
├── .gitignore
├── requirements.txt
└── README.md
```

---

## 🛠️ Getting Started

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Add your images

Place all your image folders inside `inputImages/`.  
Nested folders are fully supported.

### 3. Run the pipeline

```bash
python main.py
```

This will:
- Find all valid images recursively
- Extract metadata in parallel
- Save each result as a line in `output/metadata.jsonl`

---

## 🔍 Read Specific Metadata Fields

To print a specific EXIF field (e.g., `DateTimeOriginal`) for all images:

```bash
python readExifField.py DateTimeOriginal
```

Example output:

```
inputImages/shoots/room1/img001.jpg → DateTimeOriginal: 2023:04:15 17:22:44
inputImages/shoots/room2/img002.jpg → DateTimeOriginal: N/A
```

---

## 🧹 Git Ignore Rules

The following paths are ignored via `.gitignore`:

- `.idea/`
- `.venv/`
- `inputImages/`
- `output/metadata.jsonl`
- `__pycache__/`

This keeps your repo clean and lightweight.

---

## 📸 Use Cases

- Large-scale photo audits
- Real estate photo workflows
- Dataset preparation for computer vision
- Metadata validation & cleanup

---

## 📄 License

MIT — free to use, modify, and distribute.

---

> Built for speed, scale, and simplicity by [GhostInTheToast](https://github.com/GhostInTheToast) 🔥

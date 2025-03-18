# Subtitles Extractor

Subtitles Extractor with Translator and Notes allows users to extract subtitles from YouTube videos, translate English text to Ukrainian, and save new vocabulary for later reference, as long as creating notes and tasks for personal purposes.

## Features

✅ Extract subtitles from YouTube videos  
✅ Translate English to Ukrainian  
✅ Save and manage vocabulary 
✅ Save and manage notes and tasks

## Installation & Usage

### Option 1: Run with Docker (Recommended)

If you have Docker installed, you can run the app easily:

1. **Clone the repository**

```bash
git clone https://github.com/alina-kylymnyk/Subtitles-Extractor.git
cd Subtitles-Extractor
```

2. **Build the Docker image**

```bash
docker build -t subtitles-extractor .
```

3. **Run the container**

```bash
docker run -p 8000:8000 subtitles-extractor
```

4. **Access the app**  
   Open [http://localhost:8000](http://localhost:8000) in your browser.

### Option 2: Run Manually (Without Docker)

If you want to run the app without Docker, follow these steps:

1. **Clone the repository**

```bash
git clone https://github.com/alina-kylymnyk/Subtitles-Extractor.git
cd Subtitles-Extractor
```

2. **Create and activate a virtual environment**

```bash
python -m venv venv
source venv/bin/activate   # On Windows use: venv\Scripts\activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Run the app**

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

5. **Open in browser**  
   Visit [http://localhost:8000](http://localhost:8000)

### Project Structure

```
Subtitles-Extractor/
│── app/                         # Main application folder
│   ├── models/                  # Data models
│   │   ├── __pycache__/
│   │   ├── __init__.py
│   │   └── schemas.py           # Pydantic schemas
│   ├── routes/                  # API routes
│   │   ├── __pycache__/
│   │   ├── __init__.py
│   │   ├── subtitle_routes.py
│   │   └── translation_routes.py
│   ├── services/                # Business logic
│   │   ├── __pycache__/
│   │   ├── __init__.py
│   │   ├── subtitle_service.py
│   │   └── translation_service.py
│   ├── __pycache__/
│   ├── __init__.py
│   ├── config.py                # Configuration settings
│   └── main.py                  # FastAPI entry point
├── static/                      # Static files (CSS, JS, etc.)
│   ├── favicon.png
│   └── style.css
├── templates/                   # HTML templates
│   └── index.html
├── venv/                        # Virtual environment
├── .dockerignore                # Ignore unnecessary files for Docker
├── .gitignore                   # Ignore unnecessary files for Git
├── Dockerfile                   # Docker setup file
├── requirements.txt             # List of dependencies
└── README.md                    # Project documentation
```


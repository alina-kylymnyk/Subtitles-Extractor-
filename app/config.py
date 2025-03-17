import os

# Application settings
APP_NAME = "Subtitles Extractor"
DEBUG = os.getenv("DEBUG", "False").lower() in ("true", "1", "t")

# Static and templates directory
STATIC_DIR = "static"
TEMPLATES_DIR = "templates"

"""
Example configuration file for Storyteller.
Copy this to config.py and fill in your API keys.

This is a template showing the configuration structure without exposing
API keys or proprietary settings.
"""
import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# ============================================================================
# API Configuration
# ============================================================================
# Add your API keys in .env file:
# FAL_API_KEY=your_key_here
# ELEVENLABS_API_KEY=your_key_here

FAL_API_KEY = os.getenv("FAL_API_KEY")
ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")

# Model Endpoints (example - adjust for your API provider)
TEXT_TO_IMAGE_ENDPOINT = "your-image-generation-endpoint"
IMAGE_EDIT_ENDPOINT = "your-image-edit-endpoint"

# ============================================================================
# Image Settings (9:16 vertical format - always)
# ============================================================================
DEFAULT_IMAGE_SIZE = {
    "width": 1080,
    "height": 1920
}

# Generation Settings
DEFAULT_NUM_IMAGES = 1
ENABLE_SAFETY_CHECKER = True

# ============================================================================
# Audio Settings
# ============================================================================
# Voice Configuration (add your own voice IDs)
AVAILABLE_VOICES = {
    "default": "your-default-voice-id",
    "adam": "pNInz6obpgDQGcFmaJgB"  # Example: ElevenLabs Adam voice
}

DEFAULT_VOICE_ID = AVAILABLE_VOICES.get("default", "your-default-voice-id")
DEFAULT_MODEL_ID = "eleven_monolingual_v1"
DEFAULT_VOICE_SETTINGS = {
    "stability": 0.9,
    "similarity_boost": 0.7,
    "style": 0.0,
    "use_speaker_boost": True
}

# Audio Settings
AUDIO_FORMAT = "mp3"
AUDIO_QUALITY = "high"  # high, medium, low

# ============================================================================
# Video Settings
# ============================================================================
VIDEO_FORMAT = "mp4"
VIDEO_CODEC = "libx264"
VIDEO_QUALITY = "23"  # CRF value, lower = better quality
VIDEO_FPS = 30
TRANSITION_DURATION = 0.5  # seconds
DEFAULT_TRANSITION = "none"  # can be "none" or "crossfade"

# ============================================================================
# Directory Settings
# ============================================================================
ROOT_DIR = Path(__file__).parent.parent
OUTPUT_DIR = ROOT_DIR / os.getenv("OUTPUT_DIR", "output")
EXAMPLES_DIR = ROOT_DIR / "examples"

# Audio/Video Output Directories
AUDIO_OUTPUT_DIR = OUTPUT_DIR / "audio"
FULL_SCRIPT_AUDIO_DIR = AUDIO_OUTPUT_DIR / "full_scripts"
VIDEO_OUTPUT_DIR = OUTPUT_DIR / "videos"
ANIMATION_OUTPUT_DIR = OUTPUT_DIR / "animated_scenes"

# ============================================================================
# Scene Settings
# ============================================================================
TARGET_SCENE_DURATION = 6.0  # seconds per scene
ANIMATION_DEFAULT_DURATION = 6.0
ELEMENT_REVEAL_DURATION = 0.5

# ============================================================================
# Ensure output directories exist
# ============================================================================
OUTPUT_DIR.mkdir(exist_ok=True)
AUDIO_OUTPUT_DIR.mkdir(exist_ok=True)
FULL_SCRIPT_AUDIO_DIR.mkdir(exist_ok=True)
VIDEO_OUTPUT_DIR.mkdir(exist_ok=True)
ANIMATION_OUTPUT_DIR.mkdir(exist_ok=True)


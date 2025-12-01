# Integration Guide

This guide explains how to integrate your own API clients for image generation, audio generation, and video assembly.

## Overview

The Storyteller framework provides the core utilities for parsing scripts and managing layout patterns. You can integrate your own APIs to:

- **Generate scripts** using LLM/Chat APIs (with optional browser research)
- Generate images from prompts
- Convert narration to audio
- Assemble videos from images and audio

## Script Generation Integration (LLM/Chat APIs)

### Overview

**Scope:** LLM/Chat APIs are used **only** for research and script writing (before parsing). Once the script is generated, the parser extracts all data (narration, prompts, scenes) from the script itself.

**Workflow:**
1. **Research Phase** (Optional) - Browser automation gathers current information
2. **Script Generation** - LLM/Chat API creates the complete `.txt` script file
3. **Parser Takes Over** - Framework parses the script to extract scenes, narration, prompts, etc.

**Note:** LLM is NOT used for generating image prompts or narration during processing - those come from the parsed script.

### Interface Pattern

Create a function that generates a complete script from a topic:

```python
def generate_script(
    topic: str,
    research_enabled: bool = False,
    output_path: Path = None
) -> str:
    """
    Generate an explainer video script from a topic.
    
    Args:
        topic: The topic/subject for the explainer video
        research_enabled: If True, use browser for real-time research
        output_path: Where to save the generated script
        
    Returns:
        Generated script content as string
    """
    # Your LLM/Chat API integration here
    # Example: OpenAI, Anthropic, Google Gemini, etc.
    pass
```

### Example with OpenAI Chat API

```python
from openai import OpenAI
from pathlib import Path
import os

def generate_script(
    topic: str,
    research_enabled: bool = False,
    output_path: Path = None
) -> str:
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    
    # Optional: Research phase with browser
    research_context = ""
    if research_enabled:
        research_context = perform_research(topic)
    
    # System prompt for script generation
    system_prompt = """You are an expert explainer video script writer.
    Create a 12-scene explainer video script following the Storyteller format.
    Include: title, 12 scenes with narration, layout design, and image prompts.
    Format must match the Storyteller template exactly."""
    
    user_prompt = f"""Create an explainer video script about: {topic}
    
    {research_context if research_context else ''}
    
    Follow the Storyteller template format with:
    - Header with title, duration, format
    - 12 scenes (6 seconds each)
    - Each scene: narration, layout design, image generation prompts
    - Narration script section at the end"""
    
    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            temperature=0.7
        )
        
        script_content = response.choices[0].message.content
        
        if output_path:
            output_path.write_text(script_content, encoding='utf-8')
        
        return script_content
    except Exception as e:
        print(f"Error generating script: {e}")
        return ""
```

### Browser Integration for Real-Time Research

Use browser automation to gather current information before script generation:

```python
from playwright.sync_api import sync_playwright
from typing import List, Dict

def perform_research(topic: str) -> str:
    """
    Perform real-time research using browser automation.
    
    Args:
        topic: Topic to research
        
    Returns:
        Research context as formatted string
    """
    research_results = []
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        
        # Search for current information
        search_query = f"{topic} explainer video content 2024"
        page.goto(f"https://www.google.com/search?q={search_query}")
        page.wait_for_timeout(2000)
        
        # Extract relevant information
        # (Adjust selectors based on actual page structure)
        results = page.query_selector_all("div.g")
        for result in results[:5]:  # Top 5 results
            try:
                title = result.query_selector("h3")
                snippet = result.query_selector("span")
                if title and snippet:
                    research_results.append({
                        "title": title.inner_text(),
                        "snippet": snippet.inner_text()
                    })
            except:
                continue
        
        browser.close()
    
    # Format research context for LLM
    context = "Recent research findings:\n"
    for i, result in enumerate(research_results, 1):
        context += f"{i}. {result['title']}\n   {result['snippet']}\n\n"
    
    return context
```

### Complete Script Generation Workflow

```python
from pathlib import Path
from scripts.prompt_parser import parse_explainer_file

def create_explainer_video(topic: str, research: bool = True):
    """
    Complete workflow: Research → Generate script → Parse → Process
    
    LLM/Chat API is ONLY used for steps 1-2 (research & script writing).
    After that, parser extracts everything from the script.
    """
    # STEP 1: Research (Optional) - Browser automation
    research_context = ""
    if research:
        research_context = perform_research(topic)
    
    # STEP 2: Generate script with LLM/Chat API
    script_path = Path(f"scripts/{topic.lower().replace(' ', '_')}.txt")
    script_content = generate_script(
        topic=topic,
        research_enabled=research,
        research_context=research_context,
        output_path=script_path
    )
    
    # STEP 3: Parser extracts all data from script
    # (No more LLM calls - everything comes from parsed script)
    script_data = parse_explainer_file(script_path)
    
    # STEP 4: Process using parsed data
    # - Image prompts come from script_data['scenes'][].initial_prompt
    # - Narration comes from script_data['scenes'][].narration
    # - Layout patterns from layout_selector
    # - Continue with image/audio/video generation
    
    return script_data
```

**Key Point:** After script generation, the LLM is no longer involved. All subsequent processing uses data extracted by the parser from the script file.

### Browser Research Best Practices

1. **Respect Rate Limits** - Add delays between requests
2. **Handle Errors** - Browser automation can fail, have fallbacks
3. **Cache Results** - Don't re-research the same topics
4. **User-Agent** - Set appropriate user-agent headers
5. **Timeout Handling** - Set reasonable timeouts for page loads
6. **Headless Mode** - Use headless browsers for automation

### Example: Research-Enhanced Script Generation

```python
def generate_script_with_research(topic: str) -> str:
    """
    Generate script with real-time research enhancement.
    
    This is the ONLY place LLM/Chat API is used.
    After this, parser handles everything.
    """
    # Step 1: Research current information (Browser automation)
    print(f"Researching: {topic}...")
    research = perform_research(topic)
    
    # Step 2: Generate script with LLM/Chat API (using research context)
    print(f"Generating script with research context...")
    script = generate_script(
        topic=topic,
        research_enabled=True,
        research_context=research
    )
    
    # Step 3: Validate script format (Parser validates)
    from scripts.prompt_parser import parse_explainer_file
    try:
        # Write to temp file for validation
        temp_path = Path("temp_script.txt")
        temp_path.write_text(script)
        parsed = parse_explainer_file(temp_path)
        print(f"✅ Generated valid script with {len(parsed['scenes'])} scenes")
        print(f"✅ Parser extracted {len(parsed['scenes'])} scenes, narration, and prompts")
        return script
    except Exception as e:
        print(f"⚠️ Script validation failed: {e}")
        return script  # Return anyway, user can fix
```

**Important:** Once the script is generated and validated, the LLM/Chat API is no longer used. The parser extracts:
- Scene data
- Narration text
- Image generation prompts
- Layout design instructions
- All other script content

These are then used directly for image generation, audio generation, and video assembly (no LLM calls needed).

### Supported LLM/Chat APIs

- **OpenAI** (GPT-4, GPT-3.5)
- **Anthropic** (Claude)
- **Google** (Gemini)
- **Open Source** (Llama, Mistral via API)
- **Any Chat API** - Follow the interface pattern

### Browser Automation Tools

- **Playwright** (recommended - cross-browser, reliable)
- **Selenium** (alternative)
- **Puppeteer** (Node.js, can be called from Python)

### Configuration

```bash
# .env file
OPENAI_API_KEY=your_key_here
ANTHROPIC_API_KEY=your_key_here
GOOGLE_API_KEY=your_key_here
```

```python
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
```

---

## Image Generation Integration

### Interface Pattern

Create a class or function that takes a prompt and returns an image:

```python
def generate_image(prompt: str, output_path: Path) -> bool:
    """
    Generate an image from a prompt.
    
    Args:
        prompt: Image generation prompt
        output_path: Where to save the image
        
    Returns:
        True if successful, False otherwise
    """
    # Your API integration here
    # Example: fal.ai, DALL-E, Midjourney, etc.
    pass
```

### Example with fal.ai

```python
import fal_client
from pathlib import Path

def generate_image(prompt: str, output_path: Path) -> bool:
    try:
        result = fal_client.run(
            "fal-ai/bytedance/seedream/v4/text-to-image",
            arguments={
                "prompt": prompt,
                "image_size": "portrait_16_9",
                "num_inference_steps": 60,
            }
        )
        
        # Download and save image
        image_url = result["images"][0]["url"]
        # ... download logic ...
        
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False
```

### Using with Parser

```python
from scripts.prompt_parser import parse_explainer_file
from pathlib import Path

# Parse script
script = parse_explainer_file(Path("examples/sample.txt"))

# Generate images for each scene
for scene in script['scenes']:
    if scene.initial_prompt:
        generate_image(scene.initial_prompt, output_path)
```

## Audio Generation Integration

### Interface Pattern

Create a function that converts text to audio:

```python
def generate_audio(text: str, voice_id: str, output_path: Path) -> bool:
    """
    Generate audio from text.
    
    Args:
        text: Narration text
        voice_id: Voice identifier
        output_path: Where to save the audio file
        
    Returns:
        True if successful, False otherwise
    """
    # Your API integration here
    # Example: ElevenLabs, Azure TTS, Google TTS, etc.
    pass
```

### Example with ElevenLabs

```python
import requests
from pathlib import Path
import os

def generate_audio(text: str, voice_id: str, output_path: Path) -> bool:
    api_key = os.getenv("ELEVENLABS_API_KEY")
    
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"
    
    headers = {
        "Accept": "audio/mpeg",
        "Content-Type": "application/json",
        "xi-api-key": api_key
    }
    
    data = {
        "text": text,
        "model_id": "eleven_monolingual_v1",
        "voice_settings": {
            "stability": 0.9,
            "similarity_boost": 0.7
        }
    }
    
    try:
        response = requests.post(url, json=data, headers=headers)
        response.raise_for_status()
        
        with open(output_path, 'wb') as f:
            f.write(response.content)
        
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False
```

### Using with Narration Extractor

```python
from scripts.narration_extractor import get_all_narrations
from pathlib import Path

# Extract narrations
scenes = get_all_narrations(Path("examples/sample.txt"))

# Generate audio for each scene
for scene in scenes:
    output_path = Path(f"output/audio/scene_{scene['scene_number']:02d}.mp3")
    generate_audio(scene['narration'], "your-voice-id", output_path)
```

## Video Assembly Integration

### Interface Pattern

Combine images and audio into videos:

```python
def assemble_video(
    images: List[Path],
    audio_files: List[Path],
    output_path: Path,
    durations: List[float]
) -> bool:
    """
    Assemble video from images and audio.
    
    Args:
        images: List of image paths
        audio_files: List of audio file paths
        output_path: Output video path
        durations: Duration for each scene in seconds
        
    Returns:
        True if successful, False otherwise
    """
    # Your video assembly logic here
    # Example: FFmpeg, MoviePy, etc.
    pass
```

### Example with FFmpeg

```python
import subprocess
from pathlib import Path
from typing import List

def assemble_video(
    images: List[Path],
    audio_files: List[Path],
    output_path: Path,
    durations: List[float]
) -> bool:
    # Create FFmpeg filter complex
    # Combine images and audio with proper timing
    # See FFmpeg documentation for details
    
    cmd = [
        "ffmpeg",
        "-y",  # Overwrite output
        # ... FFmpeg arguments ...
        str(output_path)
    ]
    
    try:
        subprocess.run(cmd, check=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        return False
```

## Complete Workflow Example

```python
from scripts.prompt_parser import parse_explainer_file
from scripts.narration_extractor import get_all_narrations
from pathlib import Path

# 1. Parse script
script = parse_explainer_file(Path("examples/sample.txt"))

# 2. Generate images
images = []
for scene in script['scenes']:
    if scene.initial_prompt:
        image_path = Path(f"output/images/scene_{scene.scene_number:02d}.png")
        if generate_image(scene.initial_prompt, image_path):
            images.append(image_path)

# 3. Generate audio
audio_files = []
scenes = get_all_narrations(Path("examples/sample.txt"))
for scene in scenes:
    audio_path = Path(f"output/audio/scene_{scene['scene_number']:02d}.mp3")
    if generate_audio(scene['narration'], "your-voice-id", audio_path):
        audio_files.append(audio_path)

# 4. Assemble video
durations = [scene.duration for scene in script['scenes']]
output_video = Path("output/video/final.mp4")
assemble_video(images, audio_files, output_video, durations)
```

## Configuration

Store API keys in environment variables:

```bash
# .env file
FAL_API_KEY=your_key_here
ELEVENLABS_API_KEY=your_key_here
```

Load in your integration code:

```python
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("FAL_API_KEY")
```

## Best Practices

### General
1. **Error Handling** - Always handle API errors gracefully
2. **Rate Limiting** - Respect API rate limits
3. **Cost Management** - Monitor API usage and costs
4. **Caching** - Cache results to avoid regenerating
5. **Validation** - Validate inputs before API calls
6. **Logging** - Log API calls for debugging

### Script Generation Specific
1. **Prompt Engineering** - Craft detailed system prompts for consistent output
2. **Template Validation** - Always validate generated scripts match Storyteller format
3. **Research Caching** - Cache research results to avoid redundant browser queries
4. **Browser Ethics** - Respect robots.txt and website terms of service
5. **Fallback Logic** - Have manual script creation as fallback if generation fails
6. **Iterative Refinement** - Allow LLM to refine scripts based on validation feedback

## Resources

### Script Generation
- [OpenAI API Documentation](https://platform.openai.com/docs)
- [Anthropic API Documentation](https://docs.anthropic.com)
- [Playwright Documentation](https://playwright.dev/python)

### Media Generation
- [FFmpeg Documentation](https://ffmpeg.org/documentation.html)
- [ElevenLabs API Docs](https://elevenlabs.io/docs)
- [fal.ai Documentation](https://fal.ai/docs)

---

**Note:** These are example integrations. Adapt them to your specific API providers and requirements.


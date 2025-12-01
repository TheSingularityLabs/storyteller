"""
Parse explainer .txt files to extract prompts and scene information
"""
import re
from pathlib import Path
from typing import List, Dict, Optional


class SceneData:
    """Container for scene information"""
    def __init__(self, scene_number: int, title: str, prompt: str, duration: float = 6.0):
        self.scene_number = scene_number
        self.title = title
        self.prompt = prompt
        self.duration = duration
        self.initial_prompt = None
        self.final_prompt = None
        self._parse_prompts()
    
    def _parse_prompts(self):
        """Parse the prompt into initial and final (2-step workflow)"""
        if not self.prompt:
            return
        
        # New template format: Nano Banana Iterative Prompt with embedded initial prompt
        # Check if prompt starts with "Initial:" (new template format)
        if self.prompt.strip().startswith('Initial:'):
            # Extract the initial prompt from "Initial: [prompt] | Iteration 1: ..."
            initial_match = re.search(r'Initial:\s*([^|]+)', self.prompt)
            if initial_match:
                self.initial_prompt = initial_match.group(1).strip()
        
        # Also check for Nano Banana Iterative Prompt format
        nano_banana_match = re.search(r'Nano Banana Iterative Prompt:\s*\n\s*"([^"]+)"', self.prompt, re.DOTALL)
        if nano_banana_match:
            nano_banana_text = nano_banana_match.group(1).strip()
            # Extract the initial prompt from "Initial: [prompt] | Iteration 1: ..."
            initial_match = re.search(r'Initial:\s*([^|]+)', nano_banana_text)
            if initial_match:
                self.initial_prompt = initial_match.group(1).strip()
        
        # Legacy format: Initial Prompt: "..." and Final Prompt: "..."
        if not self.initial_prompt:
            initial_match = re.search(r'Initial Prompt:\s*\n\s*"([^"]+)"', self.prompt, re.DOTALL)
            if initial_match:
                self.initial_prompt = initial_match.group(1).strip()
        
        # Extract final prompt (legacy format)
        final_match = re.search(r'Final Prompt.*?:\s*\n\s*"([^"]+)"', self.prompt, re.DOTALL)
        if final_match:
            final_text = final_match.group(1).strip()
            # Only set if it's not the placeholder text
            if final_text and not final_text.startswith("[To be determined"):
                self.final_prompt = final_text
    
    def __repr__(self):
        return f"<Scene {self.scene_number}: {self.title}>"


def parse_explainer_file(filepath: Path) -> Dict[str, any]:
    """
    Parse an explainer .txt file and extract all scene information
    
    Returns:
        Dict with:
            - title: str
            - total_duration: float
            - format: str
            - scenes: List[SceneData]
    """
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract title from first line
    title_match = re.search(r'^#\s*(.+?)\s*-\s*\d+\s*SCENES?', content, re.MULTILINE)
    title = title_match.group(1) if title_match else "Unknown"
    
    # Extract total duration
    duration_match = re.search(r'Total Duration:\s*(\d+)\s*seconds', content)
    total_duration = int(duration_match.group(1)) if duration_match else 72
    
    # Extract scenes
    scenes = []
    
    # Pattern to match scene headers only (not the content)
    scene_pattern = r'##\s*\*?\*?SCENE\s+(\d+):\s*([^(]+)\s*\(([^)]+)\)'
    scene_matches = re.finditer(scene_pattern, content, re.MULTILINE | re.IGNORECASE)
    
    for match in scene_matches:
        scene_num = int(match.group(1))
        scene_title = match.group(2).strip()
        scene_duration_str = match.group(3).strip()
        
        # Parse duration
        duration = 6.0  # default
        if 'second' in scene_duration_str:
            dur_match = re.search(r'(\d+\.?\d*)', scene_duration_str)
            if dur_match:
                duration = float(dur_match.group(1))
        
        # Extract the full scene block
        scene_start = match.end()
        # Find next scene or end of file
        next_scene_match = re.search(r'\n##\s*\*?\*?SCENE', content[scene_start:])
        if next_scene_match:
            scene_end = scene_start + next_scene_match.start()
        else:
            scene_end = len(content)
        
        scene_content = content[scene_start:scene_end]
        
        # Extract Image Generation Prompts (2-Step Workflow)
        # Match the entire prompt block (Initial + Final)
        prompt_match = re.search(
            r'Image Generation Prompts \(2-Step Workflow\):(.*?)Animation Prompt',
            scene_content,
            re.DOTALL
        )
        
        # Fallback: try old format (Nano Banana)
        if not prompt_match:
            prompt_match = re.search(
                r'Nano Banana Iterative Prompt:\s*\n\s*"(.+)"\s*\n+Animation Prompt',
                scene_content,
                re.DOTALL
            )
        
        if prompt_match:
            prompt = prompt_match.group(1).strip()
            scene = SceneData(scene_num, scene_title, prompt, duration)
            scenes.append(scene)
    
    return {
        'title': title,
        'total_duration': total_duration,
        'format': '9:16',
        'scenes': scenes
    }


def get_scene_output_dir(base_output_dir: Path, explainer_name: str, scene_number: int) -> Path:
    """Get the output directory for a specific scene"""
    scene_dir = base_output_dir / explainer_name / f"scene_{scene_number:02d}"
    scene_dir.mkdir(parents=True, exist_ok=True)
    return scene_dir


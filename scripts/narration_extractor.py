"""
Extract narration scripts from explainer files
"""
import re
from pathlib import Path
from typing import List, Dict


def extract_narration_from_file(file_path: Path) -> List[Dict[str, str]]:
    """
    Extract narration scripts from an explainer file
    
    Args:
        file_path: Path to the explainer file
        
    Returns:
        List of dictionaries with scene info and narration
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find all scenes with narration
    # First find all scene headers (both old and new formats)
    scene_headers = re.findall(r'## \*?\*?SCENE (\d+): ([^(]+) \(([^)]+)\)', content)
    
    # Then find narration for each scene
    scenes = []
    for scene_num, title, duration in scene_headers:
        # Look for narration after this scene header (both old and new formats)
        scene_section = re.search(
            rf'## \*?\*?SCENE {scene_num}:.*?(?=## \*?\*?SCENE \d+:|$)',
            content,
            re.DOTALL
        )
        
        if scene_section:
            narration_match = re.search(r'Narration: "([^"]+)"', scene_section.group())
            if narration_match:
                scenes.append({
                    'scene_number': int(scene_num),
                    'title': title.strip(),
                    'duration': duration.strip(),
                    'narration': narration_match.group(1).strip()
                })
    
    return scenes


def get_narration_for_scene(file_path: Path, scene_number: int) -> str:
    """
    Get narration for a specific scene
    
    Args:
        file_path: Path to the explainer file
        scene_number: Scene number to extract
    
    Returns:
        Narration text for the scene
    """
    scenes = extract_narration_from_file(file_path)
    
    for scene in scenes:
        if scene['scene_number'] == scene_number:
            return scene['narration']
    
    raise ValueError(f"Scene {scene_number} not found in {file_path}")


def get_all_narrations(file_path: Path) -> List[Dict[str, str]]:
    """
    Get all narrations from an explainer file
    
    Args:
        file_path: Path to the explainer file
        
    Returns:
        List of all scenes with their narrations (limited to 12 scenes: 0-11)
    """
    scenes = extract_narration_from_file(file_path)
    
    # Filter to only get scenes 0-11 (12 scenes total)
    filtered_scenes = []
    seen_scenes = set()
    
    for scene in scenes:
        scene_num = scene['scene_number']
        if scene_num <= 11 and scene_num not in seen_scenes:
            filtered_scenes.append(scene)
            seen_scenes.add(scene_num)
    
    return filtered_scenes


if __name__ == "__main__":
    # Example usage
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python narration_extractor.py <explainer_file>")
        sys.exit(1)
    
    file_path = Path(sys.argv[1])
    if not file_path.exists():
        print(f"Error: File not found: {file_path}")
        sys.exit(1)
    
    scenes = get_all_narrations(file_path)
    print(f"Found {len(scenes)} scenes with narration:")
    
    for scene in scenes:
        print(f"\nScene {scene['scene_number']}: {scene['title']}")
        print(f"Duration: {scene['duration']}")
        print(f"Narration: {scene['narration']}")


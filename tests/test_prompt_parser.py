"""
Unit tests for prompt_parser.py
"""
import pytest
from pathlib import Path
from scripts.prompt_parser import (
    parse_explainer_file,
    SceneData,
    get_scene_output_dir
)


@pytest.fixture
def sample_explainer_path():
    """Path to sample explainer file"""
    return Path("examples/sample_explainer.txt")


@pytest.fixture
def sample_explainer_content():
    """Sample explainer content for testing"""
    return """# Sample Explainer: Test - 12 SCENES
Style: Dynamic explainer visual format
Total Duration: 72 seconds
Format: 9:16 VERTICAL

## SCENE 0: Opening Title (6 seconds) - NO NARRATION

Layout Design:
- Background: Pure white background
- Text: "Test Title" - Large, bold

Animation Prompt for AI Video Model:
"9:16 vertical format. Fade in title."

---

## SCENE 1: First Scene (6 seconds)

Narration: "This is the first scene narration."

Layout Design:
- Background: Light gray
- Text: "First Scene" - Large

Animation Prompt for AI Video Model:
"9:16 vertical format. Scene animates."

---

## NARRATION SCRIPT:

Scene 1: "This is the first scene narration."
"""


def test_parse_explainer_file_basic(sample_explainer_path):
    """Test basic parsing of explainer file"""
    if not sample_explainer_path.exists():
        pytest.skip(f"Sample file not found: {sample_explainer_path}")
    
    result = parse_explainer_file(sample_explainer_path)
    
    assert 'title' in result
    assert 'scenes' in result
    assert 'total_duration' in result
    assert 'format' in result
    assert isinstance(result['scenes'], list)
    assert len(result['scenes']) > 0


def test_parse_explainer_file_title_extraction(sample_explainer_path):
    """Test title extraction"""
    if not sample_explainer_path.exists():
        pytest.skip(f"Sample file not found: {sample_explainer_path}")
    
    result = parse_explainer_file(sample_explainer_path)
    
    assert result['title'] is not None
    assert isinstance(result['title'], str)
    assert len(result['title']) > 0


def test_parse_explainer_file_scene_count(sample_explainer_path):
    """Test that all scenes are parsed"""
    if not sample_explainer_path.exists():
        pytest.skip(f"Sample file not found: {sample_explainer_path}")
    
    result = parse_explainer_file(sample_explainer_path)
    
    # Should have 12 scenes (0-11)
    assert len(result['scenes']) == 12


def test_parse_explainer_file_scene_data_structure(sample_explainer_path):
    """Test SceneData structure"""
    if not sample_explainer_path.exists():
        pytest.skip(f"Sample file not found: {sample_explainer_path}")
    
    result = parse_explainer_file(sample_explainer_path)
    
    for scene in result['scenes']:
        assert isinstance(scene, SceneData)
        assert hasattr(scene, 'scene_number')
        assert hasattr(scene, 'title')
        assert hasattr(scene, 'prompt')
        assert hasattr(scene, 'duration')
        assert isinstance(scene.scene_number, int)
        assert isinstance(scene.title, str)
        assert isinstance(scene.duration, float)


def test_parse_explainer_file_duration(sample_explainer_path):
    """Test duration extraction"""
    if not sample_explainer_path.exists():
        pytest.skip(f"Sample file not found: {sample_explainer_path}")
    
    result = parse_explainer_file(sample_explainer_path)
    
    assert result['total_duration'] > 0
    # Default duration is 6 seconds per scene
    assert result['total_duration'] == 72.0  # 12 scenes × 6 seconds


def test_parse_explainer_file_format(sample_explainer_path):
    """Test format extraction"""
    if not sample_explainer_path.exists():
        pytest.skip(f"Sample file not found: {sample_explainer_path}")
    
    result = parse_explainer_file(sample_explainer_path)
    
    assert '9:16' in result['format'] or 'VERTICAL' in result['format'].upper()


def test_parse_explainer_file_nonexistent():
    """Test parsing non-existent file"""
    with pytest.raises(FileNotFoundError):
        parse_explainer_file(Path("nonexistent_file.txt"))


def test_get_scene_output_dir():
    """Test scene output directory generation"""
    base_dir = Path("output")
    explainer_name = "test_explainer"
    scene_number = 5
    
    result = get_scene_output_dir(base_dir, explainer_name, scene_number)
    
    assert isinstance(result, Path)
    assert "test_explainer" in str(result)
    assert "scene_05" in str(result) or "scene_5" in str(result)


def test_scene_data_attributes():
    """Test SceneData class attributes"""
    scene = SceneData(
        scene_number=0,
        title="Test Scene",
        prompt="Test prompt",
        duration=6.0
    )
    
    assert scene.scene_number == 0
    assert scene.title == "Test Scene"
    assert scene.prompt == "Test prompt"
    assert scene.duration == 6.0


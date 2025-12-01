"""
Unit tests for narration_extractor.py
"""
import pytest
from pathlib import Path
from scripts.narration_extractor import (
    extract_narration_from_file,
    get_narration_for_scene,
    get_all_narrations
)


@pytest.fixture
def sample_explainer_path():
    """Path to sample explainer file"""
    return Path("examples/sample_explainer.txt")


def test_extract_narration_from_file_basic(sample_explainer_path):
    """Test basic narration extraction"""
    if not sample_explainer_path.exists():
        pytest.skip(f"Sample file not found: {sample_explainer_path}")
    
    scenes = extract_narration_from_file(sample_explainer_path)
    
    assert isinstance(scenes, list)
    assert len(scenes) > 0
    
    for scene in scenes:
        assert 'scene_number' in scene
        assert 'title' in scene
        assert 'duration' in scene
        assert 'narration' in scene


def test_get_narration_for_scene_valid(sample_explainer_path):
    """Test getting narration for valid scene"""
    if not sample_explainer_path.exists():
        pytest.skip(f"Sample file not found: {sample_explainer_path}")
    
    narration = get_narration_for_scene(sample_explainer_path, 1)
    
    assert isinstance(narration, str)
    assert len(narration) > 0


def test_get_narration_for_scene_invalid(sample_explainer_path):
    """Test getting narration for invalid scene"""
    if not sample_explainer_path.exists():
        pytest.skip(f"Sample file not found: {sample_explainer_path}")
    
    with pytest.raises(ValueError):
        get_narration_for_scene(sample_explainer_path, 99)


def test_get_narration_for_scene_no_narration(sample_explainer_path):
    """Test getting narration for scene with no narration (scene 0)"""
    if not sample_explainer_path.exists():
        pytest.skip(f"Sample file not found: {sample_explainer_path}")
    
    narration = get_narration_for_scene(sample_explainer_path, 0)
    
    # Scene 0 typically has no narration
    assert isinstance(narration, str)
    # May be empty or have placeholder text


def test_get_all_narrations(sample_explainer_path):
    """Test getting all narrations"""
    if not sample_explainer_path.exists():
        pytest.skip(f"Sample file not found: {sample_explainer_path}")
    
    scenes = get_all_narrations(sample_explainer_path)
    
    assert isinstance(scenes, list)
    # Should have scenes 0-11 (12 scenes)
    assert len(scenes) == 12
    
    for scene in scenes:
        assert 'scene_number' in scene
        assert 'narration' in scene
        assert isinstance(scene['scene_number'], int)
        assert 0 <= scene['scene_number'] <= 11


def test_get_all_narrations_structure(sample_explainer_path):
    """Test structure of narration data"""
    if not sample_explainer_path.exists():
        pytest.skip(f"Sample file not found: {sample_explainer_path}")
    
    scenes = get_all_narrations(sample_explainer_path)
    
    for scene in scenes:
        assert isinstance(scene, dict)
        assert 'scene_number' in scene
        assert 'title' in scene
        assert 'duration' in scene
        assert 'narration' in scene
        assert isinstance(scene['narration'], str)


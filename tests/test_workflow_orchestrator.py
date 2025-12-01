"""
Unit tests for workflow_orchestrator.py
"""
import pytest
import tempfile
from pathlib import Path
from scripts.workflow_orchestrator import (
    check_output_exists,
    filter_scenes,
    handle_error,
    orchestrate_workflow
)
from scripts.prompt_parser import SceneData


@pytest.fixture
def sample_explainer_path():
    """Path to sample explainer file"""
    return Path("examples/sample_explainer.txt")


@pytest.fixture
def temp_output_dir():
    """Temporary output directory"""
    with tempfile.TemporaryDirectory() as tmpdir:
        yield Path(tmpdir)


def test_check_output_exists_true(temp_output_dir):
    """Test checking existing output"""
    output_file = temp_output_dir / "final.png"
    output_file.write_text("test")
    
    assert check_output_exists(temp_output_dir, "final.png") is True


def test_check_output_exists_false(temp_output_dir):
    """Test checking non-existing output"""
    assert check_output_exists(temp_output_dir, "final.png") is False


def test_filter_scenes_all():
    """Test filtering all scenes"""
    scenes = [
        SceneData(0, "Scene 0", "prompt", 6.0),
        SceneData(1, "Scene 1", "prompt", 6.0),
        SceneData(2, "Scene 2", "prompt", 6.0),
    ]
    
    filtered = filter_scenes(scenes, None)
    
    assert len(filtered) == 3
    assert filtered == scenes


def test_filter_scenes_specific():
    """Test filtering specific scenes"""
    scenes = [
        SceneData(0, "Scene 0", "prompt", 6.0),
        SceneData(1, "Scene 1", "prompt", 6.0),
        SceneData(2, "Scene 2", "prompt", 6.0),
    ]
    
    filtered = filter_scenes(scenes, [0, 2])
    
    assert len(filtered) == 2
    assert filtered[0].scene_number == 0
    assert filtered[1].scene_number == 2


def test_filter_scenes_empty():
    """Test filtering with empty list"""
    scenes = [
        SceneData(0, "Scene 0", "prompt", 6.0),
        SceneData(1, "Scene 1", "prompt", 6.0),
    ]
    
    filtered = filter_scenes(scenes, [])
    
    assert len(filtered) == 0


def test_handle_error_continue_true():
    """Test error handling with continue_on_error=True"""
    scene = SceneData(0, "Scene 0", "prompt", 6.0)
    error = Exception("Test error")
    
    # Mock user input - in real scenario would prompt
    # For test, we'll just verify the function exists and handles the case
    result = handle_error(scene, error, continue_on_error=True)
    
    # Function should return bool indicating whether to continue
    assert isinstance(result, bool)


def test_handle_error_continue_false():
    """Test error handling with continue_on_error=False"""
    scene = SceneData(0, "Scene 0", "prompt", 6.0)
    error = Exception("Test error")
    
    result = handle_error(scene, error, continue_on_error=False)
    
    assert result is False  # Should not continue


def test_orchestrate_workflow_basic(sample_explainer_path, temp_output_dir):
    """Test basic workflow orchestration"""
    if not sample_explainer_path.exists():
        pytest.skip(f"Sample file not found: {sample_explainer_path}")
    
    processed_scenes = []
    
    def mock_processor(scene: SceneData, output_dir: Path):
        """Mock processor that tracks processed scenes"""
        processed_scenes.append(scene.scene_number)
        output_dir.mkdir(parents=True, exist_ok=True)
        (output_dir / "final.png").write_text("test")
    
    stats = orchestrate_workflow(
        explainer_path=sample_explainer_path,
        process_scene=mock_processor,
        output_base_dir=temp_output_dir,
        skip_existing=False,
        continue_on_error=True
    )
    
    assert 'total' in stats
    assert 'completed' in stats
    assert 'skipped' in stats
    assert 'failed' in stats
    assert 'elapsed_time' in stats
    
    assert stats['total'] > 0
    assert stats['completed'] > 0
    assert isinstance(stats['elapsed_time'], float)
    assert stats['elapsed_time'] >= 0


def test_orchestrate_workflow_skip_existing(sample_explainer_path, temp_output_dir):
    """Test workflow with skip_existing=True"""
    if not sample_explainer_path.exists():
        pytest.skip(f"Sample file not found: {sample_explainer_path}")
    
    # Create existing output for scene 0
    scene_dir = temp_output_dir / "sample_explainer" / "scene_00"
    scene_dir.mkdir(parents=True, exist_ok=True)
    (scene_dir / "final.png").write_text("existing")
    
    processed_scenes = []
    
    def mock_processor(scene: SceneData, output_dir: Path):
        processed_scenes.append(scene.scene_number)
    
    stats = orchestrate_workflow(
        explainer_path=sample_explainer_path,
        process_scene=mock_processor,
        output_base_dir=temp_output_dir,
        skip_existing=True,
        continue_on_error=True
    )
    
    # Scene 0 should be skipped
    assert stats['skipped'] >= 1
    assert 0 not in processed_scenes


def test_orchestrate_workflow_nonexistent_file():
    """Test workflow with non-existent file"""
    with pytest.raises(FileNotFoundError):
        orchestrate_workflow(
            explainer_path=Path("nonexistent.txt"),
            process_scene=lambda s, d: None
        )


def test_orchestrate_workflow_specific_scenes(sample_explainer_path, temp_output_dir):
    """Test workflow with specific scene numbers"""
    if not sample_explainer_path.exists():
        pytest.skip(f"Sample file not found: {sample_explainer_path}")
    
    processed_scenes = []
    
    def mock_processor(scene: SceneData, output_dir: Path):
        processed_scenes.append(scene.scene_number)
    
    stats = orchestrate_workflow(
        explainer_path=sample_explainer_path,
        process_scene=mock_processor,
        scene_numbers=[0, 1, 2],
        output_base_dir=temp_output_dir,
        skip_existing=False
    )
    
    assert stats['total'] == 3
    assert len(processed_scenes) == 3
    assert set(processed_scenes) == {0, 1, 2}


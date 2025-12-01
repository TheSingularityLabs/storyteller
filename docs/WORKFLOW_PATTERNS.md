# Workflow Patterns

This guide explains workflow orchestration patterns for batch processing explainer scenes.

## Overview

The workflow orchestrator provides a reusable pattern for:
- Batch processing multiple scenes
- Progress tracking
- Error handling
- Skip logic for existing outputs
- Statistics and reporting

## Basic Pattern

```python
from scripts.workflow_orchestrator import orchestrate_workflow
from scripts.prompt_parser import SceneData
from pathlib import Path

def my_processor(scene: SceneData, output_dir: Path):
    """Your processing function"""
    # Your API integration here
    result = your_api.process(scene)
    save_result(result, output_dir / "final.png")

# Use the orchestrator
stats = orchestrate_workflow(
    explainer_path=Path("examples/sample.txt"),
    process_scene=my_processor
)
```

## Key Features

### 1. Progress Tracking
- Shows `[3/12] Processing Scene 5...`
- Real-time progress updates
- Time tracking

### 2. Skip Existing
- Automatically skips scenes with existing output
- Checks for `final.png` (or custom filename)
- Saves time and API costs

### 3. Error Handling
- Continues processing after errors
- Option to abort on error
- Detailed error reporting

### 4. Statistics
- Completed count
- Skipped count
- Failed count
- Elapsed time

## Use Cases

### Image Generation Workflow
```python
def generate_image(scene, output_dir):
    result = your_image_api.generate(scene.initial_prompt)
    download_image(result['url'], output_dir / "final.png")

orchestrate_workflow(
    explainer_path=Path("examples/sample.txt"),
    process_scene=generate_image,
    output_filename="final.png"
)
```

### Audio Generation Workflow
```python
def generate_audio(scene, output_dir):
    narration = extract_narration(scene)
    result = your_audio_api.generate(narration)
    save_audio(result, output_dir / "narration.mp3")

orchestrate_workflow(
    explainer_path=Path("examples/sample.txt"),
    process_scene=generate_audio,
    output_filename="narration.mp3"
)
```

### Custom Processing
```python
def custom_processor(scene, output_dir):
    # Your custom logic
    data = analyze_scene(scene)
    process_data(data, output_dir)

orchestrate_workflow(
    explainer_path=Path("examples/sample.txt"),
    process_scene=custom_processor
)
```

## Advanced Options

### Process Specific Scenes
```python
orchestrate_workflow(
    explainer_path=Path("examples/sample.txt"),
    process_scene=my_processor,
    scene_numbers=[1, 3, 5]  # Only process these scenes
)
```

### Force Regeneration
```python
orchestrate_workflow(
    explainer_path=Path("examples/sample.txt"),
    process_scene=my_processor,
    skip_existing=False  # Regenerate even if exists
)
```

### Custom Output Directory
```python
orchestrate_workflow(
    explainer_path=Path("examples/sample.txt"),
    process_scene=my_processor,
    output_base_dir=Path("custom/output")
)
```

## Error Handling

The orchestrator handles errors gracefully:

```python
def risky_processor(scene, output_dir):
    # Might fail sometimes
    result = unreliable_api.process(scene)
    save_result(result, output_dir)

orchestrate_workflow(
    explainer_path=Path("examples/sample.txt"),
    process_scene=risky_processor,
    continue_on_error=True  # Continue after errors
)
```

## Best Practices

1. **Idempotent Processing**
   - Use `skip_existing=True` to avoid reprocessing
   - Check for existing output in your function

2. **Error Recovery**
   - Handle API errors gracefully
   - Log errors for debugging
   - Consider retry logic

3. **Progress Reporting**
   - Print progress in your function
   - Use clear status messages
   - Show what's happening

4. **Resource Management**
   - Clean up temporary files
   - Manage API rate limits
   - Handle timeouts

## Integration with Other Tools

### With Image Generation
```python
from scripts.workflow_orchestrator import orchestrate_workflow
from your_image_api import generate_image

def process_scene(scene, output_dir):
    result = generate_image(scene.initial_prompt)
    save_image(result, output_dir / "final.png")

orchestrate_workflow(explainer_path, process_scene)
```

### With Audio Generation
```python
from scripts.workflow_orchestrator import orchestrate_workflow
from scripts.narration_extractor import get_narration_for_scene
from your_audio_api import generate_audio

def process_scene(scene, output_dir):
    narration = get_narration_for_scene(explainer_path, scene.scene_number)
    result = generate_audio(narration)
    save_audio(result, output_dir / "narration.mp3")

orchestrate_workflow(explainer_path, process_scene)
```

## Statistics

The orchestrator returns statistics:

```python
stats = orchestrate_workflow(explainer_path, process_scene)

print(f"Completed: {stats['completed']}")
print(f"Skipped: {stats['skipped']}")
print(f"Failed: {stats['failed']}")
print(f"Time: {stats['elapsed_time']:.2f}s")
```

## See Also

- [Integration Guide](INTEGRATION.md) - How to add API integrations
- [Workflow Example](../examples/workflow_example.py) - Complete example
- [Script Parser](../scripts/prompt_parser.py) - Scene data extraction


# API Reference

Complete reference for all functions and classes in the Storyteller framework.

**Note:** This reference covers the core framework utilities. For script generation integration (LLM/Chat APIs + browser automation), see the [Integration Guide](INTEGRATION.md).

## Script Parser (`scripts/prompt_parser.py`)

### `SceneData`

Container class for scene information.

```python
class SceneData:
    scene_number: int      # Scene number (0-11)
    title: str            # Scene title
    prompt: str           # Full prompt text
    duration: float       # Duration in seconds (default: 6.0)
    initial_prompt: str   # Extracted initial prompt (or None)
    final_prompt: str     # Extracted final prompt (or None)
```

### `parse_explainer_file(filepath: Path) -> Dict`

Parse an explainer script file and extract all scene information.

**Parameters:**
- `filepath` (Path): Path to the explainer .txt file

**Returns:**
- `Dict` with keys:
  - `title` (str): Script title
  - `total_duration` (float): Total duration in seconds
  - `format` (str): Format string (typically "9:16")
  - `scenes` (List[SceneData]): List of scene objects

**Example:**
```python
from scripts.prompt_parser import parse_explainer_file
from pathlib import Path

result = parse_explainer_file(Path("examples/sample.txt"))
print(result['title'])  # "Sample Explainer"
print(len(result['scenes']))  # 12
```

### `get_scene_output_dir(base_output_dir: Path, explainer_name: str, scene_number: int) -> Path`

Get the output directory path for a specific scene.

**Parameters:**
- `base_output_dir` (Path): Base output directory
- `explainer_name` (str): Name of the explainer (from filename)
- `scene_number` (int): Scene number

**Returns:**
- `Path`: Path to scene output directory

## Layout Selector (`scripts/layout_selector.py`)

### `suggest_patterns(scene_type, used_patterns, previous_pattern, count) -> List[Dict]`

Get layout pattern suggestions based on context.

**Parameters:**
- `scene_type` (Optional[str]): Type of scene (opening, problem, solution, etc.)
- `used_patterns` (Optional[List[int]]): List of already-used pattern IDs
- `previous_pattern` (Optional[int]): Pattern ID from previous scene
- `count` (int): Number of suggestions to return (default: 5)

**Returns:**
- `List[Dict]`: List of suggestion dicts with:
  - `pattern_id` (int): Pattern ID (1-100)
  - `name` (str): Pattern name
  - `category` (str): Pattern category
  - `weight` (str): Visual weight (light/medium/heavy)
  - `reason` (str): Why this pattern was suggested

**Example:**
```python
from scripts.layout_selector import suggest_patterns

suggestions = suggest_patterns(
    scene_type="problem",
    used_patterns=[1, 5],
    previous_pattern=12,
    count=3
)
```

### `generate_sequence(num_scenes: int, scene_types: Optional[List[str]]) -> List[Dict]`

Generate a complete non-repeating pattern sequence.

**Parameters:**
- `num_scenes` (int): Number of scenes
- `scene_types` (Optional[List[str]]): List of scene types (must match num_scenes)

**Returns:**
- `List[Dict]`: Sequence of patterns with scene_number, pattern_id, name, category, weight

**Example:**
```python
from scripts.layout_selector import generate_sequence

sequence = generate_sequence(
    12,
    ["opening", "problem", "problem", "discovery", "solution", "solution", 
     "impact", "impact", "solution", "problem", "solution", "closing"]
)
```

### `get_category(pattern_id: int) -> str`

Get the category name for a pattern ID.

**Parameters:**
- `pattern_id` (int): Pattern ID (1-100)

**Returns:**
- `str`: Category name (asymmetric, split, diagonal, circular, grid, comparison, specialty)

## Narration Extractor (`scripts/narration_extractor.py`)

### `extract_narration_from_file(file_path: Path) -> List[Dict]`

Extract all narration from an explainer file.

**Parameters:**
- `file_path` (Path): Path to explainer file

**Returns:**
- `List[Dict]`: List of scenes with:
  - `scene_number` (int)
  - `title` (str)
  - `duration` (str)
  - `narration` (str)

### `get_narration_for_scene(file_path: Path, scene_number: int) -> str`

Get narration for a specific scene.

**Parameters:**
- `file_path` (Path): Path to explainer file
- `scene_number` (int): Scene number to extract

**Returns:**
- `str`: Narration text for the scene

**Raises:**
- `ValueError`: If scene not found

### `get_all_narrations(file_path: Path) -> List[Dict]`

Get all narrations (scenes 0-11).

**Parameters:**
- `file_path` (Path): Path to explainer file

**Returns:**
- `List[Dict]`: All scenes with narration

## Workflow Orchestrator (`scripts/workflow_orchestrator.py`)

### `orchestrate_workflow(explainer_path, process_scene, ...) -> Dict`

Generic workflow orchestrator for batch processing.

**Parameters:**
- `explainer_path` (Path): Path to explainer script
- `process_scene` (Callable): User's function to process each scene
  - Signature: `process_scene(scene: SceneData, output_dir: Path) -> Any`
- `scene_numbers` (Optional[List[int]]): Specific scenes to process
- `skip_existing` (bool): Skip if output exists (default: True)
- `output_base_dir` (Path): Base output directory (default: "output")
- `output_filename` (str): Filename to check (default: "final.png")
- `continue_on_error` (bool): Continue after errors (default: True)

**Returns:**
- `Dict` with statistics:
  - `total` (int): Total scenes
  - `completed` (int): Successfully processed
  - `skipped` (int): Skipped (already exists)
  - `failed` (int): Failed scenes
  - `elapsed_time` (float): Time in seconds

**Example:**
```python
from scripts.workflow_orchestrator import orchestrate_workflow
from scripts.prompt_parser import SceneData
from pathlib import Path

def my_processor(scene: SceneData, output_dir: Path):
    # Your processing logic
    pass

stats = orchestrate_workflow(
    explainer_path=Path("examples/sample.txt"),
    process_scene=my_processor
)
```

## Constants

### Layout Patterns

- `LAYOUT_PATTERNS` (Dict[int, str]): Mapping of pattern ID to name (1-100)
- `CATEGORIES` (Dict[str, List[int]]): Category to pattern IDs mapping
- `SCENE_TYPE_RECOMMENDATIONS` (Dict[str, List[int]]): Scene type to recommended patterns
- `VISUAL_WEIGHT` (Dict[str, List[int]]): Weight classification

See `scripts/layout_selector.py` for complete pattern database.

---

For usage examples, see the [Integration Guide](INTEGRATION.md) and [Workflow Patterns](WORKFLOW_PATTERNS.md).


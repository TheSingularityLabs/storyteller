# Frequently Asked Questions

## General Questions

### What is Storyteller?

Storyteller is a framework for parsing and processing explainer video scripts. It provides utilities for extracting scene data, managing layout patterns, and orchestrating workflows.

### What can I do with this framework?

- Create scripts (manually with templates, or automatically with LLM/Chat APIs + browser research)
- Parse structured explainer video scripts
- Extract scene data, narration, and prompts
- Select layout patterns for visual variety
- Orchestrate batch processing workflows
- Integrate with your own image/audio/video APIs

### Do I need API keys to use this?

No! The core framework works without any API keys. You only need API keys if you want to add your own integrations for image generation, audio generation, or video assembly.

### What Python version do I need?

Python 3.7 or higher.

## Script Format Questions

### What format do scripts need to follow?

Scripts must follow the template format specified in [TEMPLATE_FORMAT_GUIDE.md](TEMPLATE_FORMAT_GUIDE.md). Each script includes:
- Header with metadata
- 12 scenes (typically) with narration, layout design, and prompts
- Technical specifications
- Narration script

### Can I use a different number of scenes?

Yes! The parser supports any number of scenes. The template format is designed for 12 scenes, but you can adapt it.

### What if my script doesn't match the format exactly?

The parser is flexible and handles variations, but for best results, follow the template format closely. See [TEMPLATE_FORMAT_GUIDE.md](TEMPLATE_FORMAT_GUIDE.md) for details.

## Integration Questions

### Can I generate scripts automatically?

Yes! For the full implementation, you can integrate LLM/Chat APIs for script generation. This includes:
- Browser automation for real-time research
- LLM/Chat API for script writing
- **Scope:** LLM is only used for research and script writing (before parsing). After script generation, the parser extracts all data from the script.

See [INTEGRATION.md](INTEGRATION.md) for complete examples.

### How do I add image generation?

See [INTEGRATION.md](INTEGRATION.md) for complete examples. You'll create a function that takes a prompt and saves an image, then use the workflow orchestrator to process scenes.

### Can I use multiple API providers?

Yes! The framework is provider-agnostic. You can use different APIs for different parts (e.g., DALL-E for images, ElevenLabs for audio).

### Do you provide API integrations?

No. This framework provides the structure and patterns. You add your own API integrations following the integration guide. The open-source version includes templates/guides for manual script creation. The full implementation can integrate LLM/Chat APIs and browser automation for automatic script generation.

## Usage Questions

### How do I parse a script?

```python
from scripts.prompt_parser import parse_explainer_file
from pathlib import Path

script = parse_explainer_file(Path("examples/sample_explainer.txt"))
print(f"Title: {script['title']}")
print(f"Scenes: {len(script['scenes'])}")
```

### How do I get layout pattern suggestions?

```python
from scripts.layout_selector import suggest_patterns

suggestions = suggest_patterns(
    scene_type="problem",
    used_patterns=[1, 5, 12],
    count=5
)
```

### How do I extract narration?

```python
from scripts.narration_extractor import get_all_narrations
from pathlib import Path

scenes = get_all_narrations(Path("examples/sample_explainer.txt"))
for scene in scenes:
    print(f"Scene {scene['scene_number']}: {scene['narration']}")
```

## Troubleshooting

### Parser returns "Unknown" for title

Make sure your script starts with:
```markdown
# [TOPIC]: [SUBTITLE] - 12 SCENES
```

### No scenes found

Check that your scenes use the format:
```markdown
## SCENE X: [Title] (duration seconds)
```

### Layout selector gives same patterns

Use the `--used` flag to exclude already-used patterns:
```bash
python scripts/layout_selector.py --suggest --used 1 2 3
```

### Workflow orchestrator doesn't process scenes

Make sure your processing function matches the expected signature:
```python
def my_processor(scene: SceneData, output_dir: Path):
    # Your code here
```

## Best Practices

### How do I ensure script quality?

Follow the [SCRIPT_CREATION_CHECKLIST.md](SCRIPT_CREATION_CHECKLIST.md) and review [BEST_PRACTICES.md](BEST_PRACTICES.md).

### How do I choose layout patterns?

See [LAYOUT_PATTERNS.md](LAYOUT_PATTERNS.md) for the complete catalog and selection guidelines.

### How do I structure my workflow?

See [WORKFLOW_PATTERNS.md](WORKFLOW_PATTERNS.md) for batch processing patterns and examples.

## Contributing

### How can I contribute?

See [CONTRIBUTING.md](../CONTRIBUTING.md) for guidelines. We welcome:
- Bug fixes
- Documentation improvements
- New layout patterns
- Example scripts
- Parser improvements

### Can I add API integrations?

We keep API integrations private to maintain framework flexibility. However, you can share integration examples or patterns in the Integration Guide.

## License

### What license is this under?

MIT License - See [LICENSE](../LICENSE) for details.

### Can I use this commercially?

Yes! MIT License allows commercial use.

---

**Still have questions?** Open an issue on GitHub or check the documentation guides.


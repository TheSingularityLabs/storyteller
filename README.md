# Storyteller - Open Source Framework

A Python codebase for parsing and processing explainer video scripts. Provides utilities for extracting scene data, managing layout patterns, and orchestrating video creation workflows.

## 🎯 What's Included

✅ **Core Utilities**
- Script parser for extracting scene data from structured text files
- Layout pattern selector (100 unique patterns)
- Narration extractor
- Workflow orchestrator (batch processing pattern)
- Template format specifications

✅ **Documentation**
- Complete template format guide
- Layout pattern catalog
- Best practices for script creation
- Script creation checklist

✅ **Templates**
- Blank template for creating new scripts
- Example scripts demonstrating the format

## 🔌 Extending the Framework

This framework provides the core utilities. To create complete videos, you'll need to add your own integrations for:

- **Script Generation** (Optional) - Integrate LLM/Chat APIs for research and script writing only (before parsing). After script generation, parser extracts all data from the script.
- **Image Generation** - Connect your preferred image generation API
- **Audio Generation** - Integrate your text-to-speech service
- **Video Assembly** - Use FFmpeg or your video processing tool

**Why?** This keeps the framework provider-agnostic. You can use any APIs you prefer (OpenAI, Claude, fal.ai, DALL-E, ElevenLabs, Azure TTS, etc.).

See the [Integration Guide](docs/INTEGRATION.md) for examples and patterns.

## 🚀 Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/storyteller.git
cd storyteller

# Install dependencies (minimal - no API clients)
pip install -r requirements.txt
```

### Basic Usage

```bash
# Parse an explainer script
python scripts/prompt_parser.py examples/sample_explainer.txt

# Get layout pattern suggestions
python scripts/layout_selector.py --suggest --type problem

# Generate a layout sequence for 12 scenes
python scripts/layout_selector.py --generate 12

# Extract narration from a script
python scripts/narration_extractor.py examples/sample_explainer.txt

# Use workflow orchestrator (see examples/workflow_example.py)
python scripts/workflow_orchestrator.py examples/sample_explainer.txt
```

## 📖 Documentation

- **[Template Format Guide](docs/TEMPLATE_FORMAT_GUIDE.md)** - Complete specification for script format
- **[Layout Patterns](docs/LAYOUT_PATTERNS.md)** - 100 unique layout patterns
- **[Best Practices](docs/BEST_PRACTICES.md)** - Quality standards and tips
- **[Script Creation Checklist](docs/SCRIPT_CREATION_CHECKLIST.md)** - Step-by-step guide
- **[Workflow Patterns](docs/WORKFLOW_PATTERNS.md)** - Batch processing and orchestration patterns
- **[Workflow Flowchart](docs/WORKFLOW_FLOWCHART.md)** - Visual workflow diagram
- **[Integration Guide](docs/INTEGRATION.md)** - How to add your own API integrations
- **[API Reference](docs/API_REFERENCE.md)** - Complete function and class documentation
- **[FAQ](docs/FAQ.md)** - Frequently asked questions
- **[Troubleshooting](docs/TROUBLESHOOTING.md)** - Common issues and solutions

## 💻 Usage

Import and use the utilities in your own code:

```python
from scripts.prompt_parser import parse_explainer_file
from scripts.layout_selector import generate_sequence

# Parse a script
script = parse_explainer_file(Path("my_script.txt"))

# Get layout patterns
patterns = generate_sequence(12)
```

## 🏗️ Core Components

1. **Script Parser** (`scripts/prompt_parser.py`)
   - Parses structured explainer scripts
   - Extracts scene data, narration, prompts
   - Validates script format

2. **Layout Selector** (`scripts/layout_selector.py`)
   - 100 unique layout patterns
   - Intelligent pattern selection
   - Prevents repetition across scenes

3. **Narration Extractor** (`scripts/narration_extractor.py`)
   - Extracts narration text from scripts
   - Scene-by-scene extraction
   - Format validation

4. **Workflow Orchestrator** (`scripts/workflow_orchestrator.py`)
   - Generic batch processing pattern
   - Progress tracking and error handling
   - Skip logic for existing outputs
   - Statistics and reporting

### Template Format

Every script follows a structured format:

```markdown
# [TOPIC]: [SUBTITLE] - 12 SCENES
Style: Dynamic explainer visual format
Total Duration: 72 seconds
Format: 9:16 VERTICAL

## SCENE 0: Opening Title (6 seconds)
Narration: "[Text]"
Layout Design: ...
Animation Prompt: ...
```

See [Template Format Guide](docs/TEMPLATE_FORMAT_GUIDE.md) for complete specification.

## 🔌 Integration

Want to add image generation, audio generation, or video assembly?

See [docs/INTEGRATION.md](docs/INTEGRATION.md) for:
- How to integrate your own APIs
- Interface patterns
- Example implementations

## 📋 Requirements

- Python 3.8+ (tested on 3.8-3.12)
- Standard library only (no external API dependencies)

**For development/testing:**
- pytest >= 7.0.0
- pytest-cov >= 4.0.0

Optional dependencies for integrations:
- Image generation API client (your choice)
- Audio generation API client (your choice)
- Video processing library (FFmpeg, etc.)

## 📝 Examples

See `examples/` folder for sample scripts demonstrating the format:
- `sample_explainer.txt` - Storyteller framework overview
- `product_launch_explainer.txt` - Problems Storyteller solves
- `target_audience_explainer.txt` - Who Storyteller is for

Each example follows the Storyteller template format and demonstrates different use cases.

## 🧪 Testing

Run the test suite:

```bash
# Install test dependencies
pip install -r requirements.txt

# Run all tests
pytest tests/ -v

# Run with coverage
pytest tests/ --cov=scripts --cov-report=html
```

Tests cover:
- Script parsing and validation
- Layout pattern selection
- Narration extraction
- Workflow orchestration

## 🤝 Contributing

Contributions welcome! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

**Before submitting:**
1. Run tests: `pytest tests/ -v`
2. Ensure all tests pass
3. Follow code style guidelines
4. Update documentation if needed

CI/CD runs automatically on push/PR via GitHub Actions.

## 📄 License

MIT License - See [LICENSE](LICENSE) for details.

## 🙏 Acknowledgments

This framework was developed as part of [thesingularitylabs.xyz](https://thesingularitylabs.xyz) content creation workflow. The open-source version shares the core patterns and utilities while keeping implementation-specific code private.

## 📚 Related Resources

- [Template Format Guide](docs/TEMPLATE_FORMAT_GUIDE.md)
- [Layout Patterns Catalog](docs/LAYOUT_PATTERNS.md)
- [Best Practices](docs/BEST_PRACTICES.md)
- [Integration Guide](docs/INTEGRATION.md)

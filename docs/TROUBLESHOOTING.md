# Troubleshooting Guide

Common issues and solutions when using the Storyteller framework.

## Parser Issues

### "Unknown" Title

**Problem:** Parser returns "Unknown" for script title.

**Solution:** Ensure your script starts with:
```markdown
# [TOPIC]: [SUBTITLE] - 12 SCENES
```

The parser looks for this exact format at the start of the file.

### No Scenes Found

**Problem:** Parser finds 0 scenes.

**Possible Causes:**
1. Scene headers don't match expected format
2. File encoding issues
3. Missing scene markers

**Solution:**
- Check scene format: `## SCENE X: [Title] (duration seconds)`
- Ensure file is UTF-8 encoded
- Verify scene markers are present

**Example of correct format:**
```markdown
## SCENE 1: Problem Introduction (6 seconds)
```

### Scene Data Missing

**Problem:** Scenes found but missing prompts or narration.

**Solution:**
- Ensure prompts are in the expected format
- Check that narration uses: `Narration: "[text]"`
- Verify prompts are between scene header and next scene

## Layout Selector Issues

### Same Patterns Repeated

**Problem:** Layout selector suggests patterns you've already used.

**Solution:** Use the `--used` flag:
```bash
python scripts/layout_selector.py --suggest --used 1 5 12 46
```

Or in code:
```python
suggestions = suggest_patterns(
    used_patterns=[1, 5, 12, 46],
    count=5
)
```

### No Suggestions for Scene Type

**Problem:** No patterns suggested for your scene type.

**Solution:**
- Check scene type spelling (opening, problem, solution, etc.)
- Use `None` for scene_type to get all patterns
- Review available types in `SCENE_TYPE_RECOMMENDATIONS`

### Pattern ID Out of Range

**Problem:** Error about pattern ID > 100.

**Solution:**
- Valid pattern IDs are 1-100
- Check your pattern ID before using
- Use `get_category()` to validate

## Narration Extractor Issues

### Narration Not Found

**Problem:** Extractor returns empty narration.

**Possible Causes:**
1. Narration format incorrect
2. Scene number mismatch
3. File encoding issues

**Solution:**
- Use format: `Narration: "[text]"`
- Ensure scene numbers match
- Check file encoding (UTF-8)

### Wrong Scene Narration

**Problem:** Getting narration from wrong scene.

**Solution:**
- Verify scene numbers in script match expected
- Check for duplicate scene numbers
- Use `extract_narration_from_file()` to see all scenes

## Workflow Orchestrator Issues

### Function Not Called

**Problem:** Your processing function never gets called.

**Possible Causes:**
1. Function signature incorrect
2. Output already exists (if skip_existing=True)
3. Script parsing failed

**Solution:**
- Function must be: `def my_func(scene: SceneData, output_dir: Path)`
- Check if output files already exist
- Verify script parses correctly first

### Errors Not Handled

**Problem:** Workflow stops on first error.

**Solution:**
- Set `continue_on_error=True` (default)
- Handle errors in your processing function
- Check error messages for details

### Wrong Output Directory

**Problem:** Files saved to wrong location.

**Solution:**
- Specify `output_base_dir` parameter
- Check `explainer_name` matches your script filename
- Verify directory permissions

## Integration Issues

### API Calls Not Working

**Problem:** Your API integration doesn't work.

**Solution:**
- Check API keys are set in environment variables
- Verify API endpoint URLs
- Test API calls outside the framework first
- Check error messages for API-specific issues

### Image/Audio Not Saving

**Problem:** Generated content not saved to disk.

**Solution:**
- Ensure `output_dir` exists (create if needed)
- Check file permissions
- Verify save path is correct
- Handle API response format correctly

## File Format Issues

### Encoding Errors

**Problem:** Special characters not displaying correctly.

**Solution:**
- Save scripts as UTF-8
- Use `encoding='utf-8'` when reading files
- Avoid special characters in filenames

### Path Issues

**Problem:** File not found errors.

**Solution:**
- Use `Path` objects from `pathlib`
- Use relative paths from project root
- Check file exists before processing

## Performance Issues

### Slow Parsing

**Problem:** Parser takes too long.

**Solution:**
- Large files may be slow - this is normal
- Check file size (should be < 1MB typically)
- Profile if needed for very large scripts

### Memory Issues

**Problem:** Out of memory errors.

**Solution:**
- Process scenes one at a time
- Don't load all scenes into memory at once
- Use workflow orchestrator for batch processing

## Getting Help

### Still Having Issues?

1. **Check Documentation:**
   - [Template Format Guide](TEMPLATE_FORMAT_GUIDE.md)
   - [Integration Guide](INTEGRATION.md)
   - [FAQ](FAQ.md)

2. **Review Examples:**
   - Check `examples/` folder
   - Review workflow examples

3. **Open an Issue:**
   - Describe the problem
   - Include error messages
   - Share relevant code snippets

---

**Common Solutions Summary:**
- ✅ Check file format matches template
- ✅ Verify function signatures
- ✅ Use UTF-8 encoding
- ✅ Check file paths and permissions
- ✅ Review error messages carefully


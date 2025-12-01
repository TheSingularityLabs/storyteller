# Best Practices

Production quality standards and optimization strategies for the Storyteller framework.

## Text Balance & Clarity

### The Golden Rules
1. **Maximum 1 main headline per scene** (5-10 words)
2. **Limit text labels to 3-5 total** (more text = more typo risk)
3. **Prefer icons over text labels** (visual > verbal when possible)
4. **Make text BIG and readable** (but don't overcrowd)
5. **Rule of thumb**: If you need text to explain it, simplify the visual

### Text Positioning Standards

**NEVER place text over main visual elements**
- Text should be in clear, dedicated areas
- Main visuals deserve unobstructed space

**Use safe zones consistently**
- Top 20% of frame (above main content)
- Bottom 15% of frame (below main content)
- Left/right margins for side-aligned text

**Avoid center placement**
- Center is reserved for primary visual elements
- Text should frame the image, not cover it

**Text positioning examples**
```
✓ Good: TOP-LEFT corner (safe zone)
✓ Good: BOTTOM FULL-WIDTH banner
✓ Good: LEFT-ALIGNED in upper third
✗ Bad: CENTERED mid-frame (blocks visuals)
✗ Bad: Overlaying main character
```

## 2D Flat Silhouette Requirements

### All Human Characters Must Be
- **2D flat silhouettes** (not realistic people)
- **Minimalist geometric forms** (simple shapes)
- **Stylized icons** (clean, abstract)
- **No facial details** (suggestion only)

### Correct Descriptions in Prompts
```
✓ "2D flat silhouette celebrating with arms up"
✓ "minimalist geometric figure at computer"
✓ "stylized person icon showing confusion"
✓ "simple flat form with raised arms"

✗ "realistic person with facial expression"
✗ "detailed character illustration"
✗ "photorealistic human figure"
```

### Why This Matters
- Maintains minimalist aesthetic
- Reduces generation complexity
- Ensures style consistency
- Works better with AI models
- Scales to any size without quality loss

## Layout Variety Guidelines

### The Variety Imperative
Never repeat the same layout pattern across scenes. Each scene should have unique visual composition.

### 10+ Layout Patterns to Use
1. **Asymmetric** - Right-side heavy, left-aligned text
2. **Vertical Split** - 50/50 or 30/70 left-right division
3. **Horizontal Split** - Top-bottom division (usually unequal)
4. **Diagonal Cascade** - Elements flowing corner-to-corner
5. **Circular Orbit** - Elements orbiting around center
6. **Radial Expansion** - Elements radiating from center
7. **Two-Column** - Left metrics/data, right human reaction
8. **Hero-Centered** - Large central element, corner badges
9. **L-Shaped** - Vertical + horizontal element arrangement
10. **Before/After** - Left vs right comparison
11. **Four-Quadrant** - 2x2 grid with central connector
12. **Timeline Journey** - Diagonal bottom-left to top-right

### Pattern Selection Strategy
- **Problem scenes** (1-3): Asymmetric, cascade, split
- **Discovery scenes** (4-5): Radial, hero-centered, circular
- **Benefit scenes** (6-7): Two-column, comparison, split
- **Detail scenes** (8-9): Grid, L-shaped, trajectory
- **Impact scenes** (10): Before/after, burst, celebration

### Layout Variety Checklist
```
□ Each scene uses different pattern
□ Text position varies (not all centered)
□ Element counts differ (not all 4-icon orbits)
□ Asymmetry is balanced across video
□ Visual rhythm has variety
```

## Typo Prevention Strategies

### Minimize Text = Minimize Typos
The fewer text labels you include, the lower your error rate.

### Text Reduction Tactics
1. **Replace labels with icons**
   - Instead of: "Fast" clock icon + "Slow" hourglass
   - Use: Clock icon + Hourglass icon (visual tells the story)

2. **Use symbols over words**
   - Instead of: "Expensive" badge
   - Use: "$$$" symbol

3. **Single-word labels only**
   - ✓ "2006", "85%", "100x"
   - ✗ "Cost Effective Solution", "High Performance"

4. **Let narration carry meaning**
   - Narration explains details
   - Visuals reinforce with minimal text

### High-Risk Text Areas
- Long phrases (3+ words)
- Technical terminology
- Numbers with units ("100M+ Users")
- Abbreviations that could be wrong

### Pre-Generation Checklist
Before running Nano Banana prompts:
```
□ Spell-check all text in prompts
□ Verify numbers are correct
□ Confirm proper capitalization
□ Check for consistent terminology
□ Read entire prompt aloud
```

## Prompt Quality Standards

### Nano Banana Iterative Prompts

**Structure compliance**
- Must follow 4-step format: Initial | Iteration 1 | Iteration 2 | Iteration 3
- Each step separated by " | " delimiter
- Clear instructions for each iteration

**Iteration focus areas**
- **Iteration 1**: "Fix any text typos, ensure [key element] clearly conveys [message], verify [arrangement] is balanced"
- **Iteration 2**: "Enhance minimalism - simplify all icons to basic geometric shapes, ensure consistent line weights, verify person is flat 2D silhouette"
- **Iteration 3**: "Control consistency - maintain pure white minimalist aesthetic, ensure all icons same visual style, verify background doesn't compete with foreground"

**Specificity requirements**
- Name exact colors (e.g., "pure white background", "vibrant green #76B900")
- Specify exact positions (e.g., "top-right corner", "60% of frame")
- Describe 2D figures explicitly (e.g., "2D flat silhouette", "minimalist geometric form")
- Include opacity percentages for backgrounds (e.g., "15% opacity")

### Animation Prompts for AI Video Model (MANDATORY)

**MANDATORY FORMAT:**
- **Start with**: "Animate ONLY the elements visible in the static image"
- **Reference elements as "already visible"** - describe what exists, then animate it
- **Smooth, gradual animations** throughout the full 6 seconds (no "quickly" or "rapidly")
- **Distributed timing** - animations happen continuously across the 6 seconds
- **End with**: "Auto-switch to next scene after 6 seconds"
- **No new elements** - only animate what's in the static image

**Essential elements (in order):**
1. Format declaration: "9:16 vertical format"
2. Mandatory start: "Animate ONLY the elements visible in the static image"
3. Background description (including gradient/color)
4. Element animation sequence (reference as "already visible", then animate)
5. Timing specifications (smooth, distributed across 6 seconds)
6. Mandatory end: "Auto-switch to next scene after 6 seconds"

**Timing Guidelines:**
- Text: 0-1.5s (smooth fade in)
- Primary visuals: 1-2.5s (smooth materialization)
- Secondary elements: 2-4s (smooth appearance)
- Continuous effects: 2.5-6s (smooth pulsing/flowing)
- All animations overlap and run throughout the full 6 seconds

**Example Structure:**
```
"9:16 vertical format. Animate ONLY the elements visible in the static image. [Background]. [Text element] already visible - animate it smoothly fading in (0-1.5s). [Visual element] already visible - animate it smoothly materializing (1-2.5s). [Secondary element] already visible - animate it smoothly appearing (2-4s) and subtly pulsing (3-6s). All elements animate smoothly throughout the full 6 seconds. Do NOT add any new elements. Only animate what exists in the static image. Camera is static, centered position. Clean, minimalist aesthetic. Duration: 6 seconds. Auto-switch to next scene after 6 seconds."
```
6. Closing notes ("static background", "clean minimalist presentation")

**Consistency with Nano Banana**
- Animation prompt must reflect refined image from Nano Banana
- Incorporate details from Iteration 3 (final refined version)
- Maintain same visual vocabulary

## Quality Assurance Checklist

### Before Generation
```
□ Narration is 50-70 words per 6s scene
□ All humans described as 2D flat silhouettes
□ Text labels limited to 3-5 per scene
□ Each scene uses different layout pattern
□ Text positioned in safe zones
□ Prompts include all 4 iterations
□ No spelling errors in prompts
```

### During Generation
```
□ Initial image matches layout description
□ Iteration 1 fixes any typos
□ Iteration 2 achieves minimalism
□ Iteration 3 ensures style consistency
□ Animation matches refined static image
□ Motion is smooth and purposeful
```

### After Generation
```
□ All text readable on mobile (9:16)
□ Humans are flat silhouettes (not realistic)
□ Consistent visual style across scenes
□ No visual clutter or overlap
□ Animations transition smoothly
□ Total duration is 60-72 seconds
```

## Performance Optimization

### Generation Speed
- Run Nano Banana iterations sequentially (don't skip)
- Batch similar scenes together
- Keep prompt complexity moderate

### Cost Optimization
- Perfect your prompts before generating
- Use iterations to refine, not restart
- Reuse successful pattern templates

### Quality vs Speed Trade-offs
- Fast: Skip Iteration 3 (acceptable for drafts)
- Balanced: Run all 4 steps (recommended)
- Premium: Add extra refinement round if needed

## Common Pitfalls to Avoid

### Content Issues
- ❌ Abstract language instead of specific examples
- ❌ Too much text causing information overload
- ❌ Realistic characters breaking minimalist style
- ❌ Repetitive layouts becoming monotonous
- ❌ Text covering main visual elements

### Technical Issues
- ❌ Prompts missing key details (position, size, style)
- ❌ Skipping iterations to save time
- ❌ Inconsistent terminology across scenes
- ❌ Animation prompts not matching refined images
- ❌ Wrong aspect ratio (16:9 instead of 9:16)

### Production Issues
- ❌ Narration too long for scene duration
- ❌ Voice-over not synced with visuals
- ❌ Background music overpowering narration
- ❌ Not testing on mobile device
- ❌ Exporting at wrong specifications

## Excellence Standards

### Minimum Viable Quality (MVQ)
- All text is readable
- 2D silhouettes throughout
- No major typos
- Basic layout variety
- 60-72 second duration

### Production Quality (Recommended)
- Text perfectly positioned in safe zones
- Maximum 3-5 labels per scene
- 10+ unique layout patterns
- All 4 Nano Banana iterations
- Smooth animations
- Mobile-tested

### Premium Quality (Best Practice)
- Every detail intentional
- Perfect text-visual balance
- Innovative layout compositions
- Extra refinement rounds
- Professional voice-over
- Custom background music
- Brand-perfect styling

## Update Protocol

When the framework evolves:
1. Update this document first
2. Revise template to match
3. Create example demonstrating new feature
4. Test with real project
5. Document lessons learned

## Resources

- Full system guide: `../EXPLAINER_VIDEO_GUIDE.md`
- Usage workflow: `USAGE.md`
- Examples: `../examples/`
- Template: `../templates/blank_explainer_template.txt`


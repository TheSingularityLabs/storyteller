# Style Preservation Guide
## Maintaining Visual Consistency Across All Scenes

**Reference Quality:** Scene 3 (Atlas Breakthrough) & Scene 4 (Timeline Evolution)

**⚠️ MANDATORY:** All scripts must follow the comprehensive template format. See `TEMPLATE_FORMAT_GUIDE.md` for complete requirements.

---

## Core Style Principles

### 1. **Background**
- ✅ Very subtle light gray gradient (#F8F9FA to #FFFFFF)
- ✅ Almost white - barely visible gradient
- ❌ NO pure white or dark gray backgrounds
- **Example:** Scene 3's mountain scene has subtle gray that doesn't compete with content

### 2. **Text Treatment**
- ✅ ALL text in BLACK (#000000)
- ✅ Bold sans-serif for headlines
- ✅ Clean, readable, professional
- ❌ NO colored text boxes (green, blue, red rounded rectangles)
- ❌ NO hex codes visible as text
- **Example:** Scene 4's "A decade of evolution" - clean black text, no boxes

### 3. **Color Usage**
- ✅ Strategic accent colors ONLY for brand elements:
  - Boston Dynamics: Orange (#FF6B35)
  - Figure AI: Blue (#3B82F6)
  - Tesla: Red (#E82127)
  - Timeline/Progress: Purple (#8B5CF6)
- ✅ Colors applied to icons/badges, not text backgrounds
- ❌ NO bright green/yellow boxes
- ❌ NO hex codes showing as visible text
- **Example:** Scene 3's orange robot - color is IN the element, not around it

### 4. **Layout Elements**
- ✅ Subtle lines and outlines (3-5% opacity)
- ✅ Clean geometric shapes
- ✅ Minimalist icons
- ✅ Each scene has UNIQUE layout pattern (mountain, timeline, radial, etc.)
- ❌ NO bold/thick lines dominating the scene
- **Example:** Scene 3's mountain outline at 3% opacity - barely visible but adds depth

### 5. **Depth & Shadows**
- ✅ Subtle soft shadows beneath elements
- ✅ Professional polish without being 3D-heavy
- ✅ Consistent shadow direction
- ❌ NO heavy drop shadows or glossy effects
- **Example:** Scene 3's robot has subtle shadow creating depth

---

## Common Mistakes to Avoid

### ❌ Mistake #1: Hex Codes Showing as Text
**Problem:** "#F8F9FA", "#3B82F6", "DFF6B35" appearing on the image  
**Fix:** Remove ALL hex code text - colors should be applied, not shown

### ❌ Mistake #2: Colored Text Boxes
**Problem:** Bright green/red/blue rounded rectangles with text  
**Fix:** Use clean BLACK text without boxes, like Scene 4's "Research → Reality"

### ❌ Mistake #3: Background Too Dark
**Problem:** Gray background competing with content  
**Fix:** Very subtle gradient, almost white like Scene 3

### ❌ Mistake #4: Bold Blue/Bright Lines
**Problem:** Thick colored lines dominating the layout  
**Fix:** Subtle gray lines (3-5% opacity) like Scene 3's mountain outline

### ❌ Mistake #5: Too Many Colors
**Problem:** Rainbow of colors making it look busy  
**Fix:** Light background + black text + ONE strategic accent color per scene

---

## Scene-by-Scene Style Checklist

Use this checklist for EVERY scene's final refinement:

```
Refine [LAYOUT TYPE] infographic with Scene 3 and 4 style reference:

✓ REMOVE all hex codes (should NEVER appear as visible text)
✓ Change background to very subtle light gray gradient like Scene 3 (almost white)
✓ Ensure [SCENE TITLE] is bold, prominent at top in BLACK text
✓ Verify [MAIN ELEMENTS] are clearly positioned with correct layout
✓ Check that [BRAND COLOR] is applied to icons/badges, not text backgrounds
✓ Confirm NO colored boxes around text - use clean BLACK text only
✓ Ensure all labels/annotations are in BLACK text
✓ Add subtle lines/outlines at low opacity (3-5%) if needed for structure
✓ Match Scene 3's professional polish: subtle shadows, clean composition
✓ Balance text-to-visual ratio like reference images
✓ Verify [UNIQUE LAYOUT PATTERN] is preserved while maintaining style
✓ Overall feel: light background, black text, strategic single accent color
```

---

## Template for Final Refinement Prompts

```
Refine [unique layout name] infographic with Scene 3 and 4 style reference:
- REMOVE all hex codes - these should never appear as visible text
- Change background to MUCH lighter - very subtle light gray gradient like Scene 3 Atlas (almost white, barely visible)
- Ensure '[Scene Title]' is bold, prominent at [position] in BLACK text
- Verify [list key elements with correct positioning]
- Check that [brand color name] is applied to [specific elements], not text backgrounds  
- Confirm NO bright colored boxes around text - use clean BLACK text
- Add subtle [lines/outlines/patterns] at low opacity (3-5%) for structure
- Match Scene 3's professional polish: subtle shadows, clean minimalist aesthetic
- Balance text-to-visual ratio like Scene 3 and 4
- Overall: light background, BLACK text throughout, strategic [single color] accent
```

## 📋 **Template Format Integration**

### **Nano Banana Iterative Prompt Structure**
Every scene MUST include this 3-step iteration process:

```
"Initial: [Initial prompt] | Iteration 1: [First iteration] | Iteration 2: [Second iteration] | Iteration 3: [Final iteration]"
```

### **Animation Prompt Structure**
Every scene MUST include animation instructions:

```
"9:16 vertical format. [Background details]. [Main elements] materialize/fade in. [Supporting elements] appear. [Corner elements] fade in. [Background pattern] emerges. Sequential fade-ins at 0.5s intervals, [layout pattern], minimal motion, clean minimalist presentation, static background."
```

### **Layout Design Requirements**
Every scene MUST include:
- Background specification
- Text positioning and typography
- Visual elements with detailed descriptions
- Aesthetic description

---

## Quick Reference: Scene 3 & 4 Characteristics

### Scene 3 - Atlas Breakthrough (Mountain Peak)
- Very subtle light gray gradient background
- Black text: "2013: The Atlas Breakthrough"
- Orange Boston Dynamics robot (brand color applied)
- Mountain outline at 3% opacity (barely visible)
- NO hex codes visible
- Clean minimalist aesthetic
- Professional polish with subtle shadows

### Scene 4 - Timeline Evolution (Horizontal Timeline)
- Clean light background with subtle horizontal lines
- Black text: "A decade of evolution", "Research → Reality"
- Strategic orange color pops on timeline milestones
- Mathematical precision in spacing
- NO colored boxes - just clean text with arrow
- Minimalist icons evenly spaced
- Professional composition

---

## Color Palette Reference

**Backgrounds:**
- Light Gray Gradient: #F8F9FA to #FFFFFF (very subtle)
- Use sparingly - almost white appearance

**Text:**
- All Text: #000000 (Black)
- NO colored text backgrounds

**Strategic Accents (use ONE per scene):**
- Boston Dynamics: #FF6B35 (Orange)
- Figure AI: #3B82F6 (Tech Blue)
- Tesla: #E82127 (Red)
- Timeline/Progress: #8B5CF6 (Purple)
- Positive/Success: #10B981 (Green) - use for arrows/indicators only

**Lines & Outlines:**
- Subtle Elements: 3-5% opacity in light gray
- Never bold or thick

---

## Example Workflow

**Initial Generated → Review → Final with Style Checklist**

**Initial Issues:**
- ❌ Hex codes showing: "#F8F9FA"
- ❌ Green box around text
- ❌ Background too dark
- ❌ Blue text instead of black

**Apply Style Checklist:**
```
Remove hex codes → Check ✓
Light background → Check ✓  
Black text throughout → Check ✓
No colored boxes → Check ✓
Strategic accent color only → Check ✓
Subtle shadows → Check ✓
```

**Final Result:**
- ✅ Matches Scene 3 & 4 quality
- ✅ Maintains unique layout identity
- ✅ Professional polish
- ✅ Visual consistency

---

## Share This Guide

**When collaborating:**
1. Share Scene 3 & 4 final images as reference
2. Share this style guide
3. Emphasize: "Match the STYLE, not the LAYOUT"
4. Use the checklist for every scene

**Key Message:**
> "Light background, black text, strategic single accent color, subtle shadows, clean minimalist aesthetic - just like Scene 3 and 4."

---

**Created:** 2025-10-11  
**Reference Quality:** Scene 3 (Atlas) & Scene 4 (Timeline)  
**Purpose:** Maintain visual consistency across all 12 scenes while preserving unique layouts


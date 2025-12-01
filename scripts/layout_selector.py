"""
Intelligent layout pattern selector to ensure visual variety
Prevents repetition and suggests optimal layout patterns
"""
import random
from typing import List, Dict, Optional, Set
from pathlib import Path
import json


# Layout pattern database (ID: Name)
LAYOUT_PATTERNS = {
    # Asymmetric (1-15)
    1: "Right-Heavy Asymmetric",
    2: "Left-Heavy Asymmetric",
    3: "Top-Heavy Asymmetric",
    4: "Bottom-Heavy Asymmetric",
    5: "Diagonal Heavy (Top-Left to Bottom-Right)",
    6: "Diagonal Heavy (Top-Right to Bottom-Left)",
    7: "Corner Focus (Top-Left)",
    8: "Corner Focus (Bottom-Right)",
    9: "Z-Pattern Asymmetric",
    10: "Inverted Z-Pattern",
    11: "C-Curve Asymmetric",
    12: "S-Curve Flow",
    13: "Stair-Step Asymmetric",
    14: "Cluster & Isolate",
    15: "Weighted Corners (3:1)",
    
    # Split (16-30)
    16: "Vertical 50/50",
    17: "Vertical 30/70",
    18: "Vertical 70/30",
    19: "Vertical 20/80",
    20: "Vertical 60/40",
    21: "Horizontal 50/50",
    22: "Horizontal 30/70",
    23: "Horizontal 70/30",
    24: "Horizontal 40/60",
    25: "Triple Vertical Split (33/33/33)",
    26: "Triple Horizontal Split",
    27: "Golden Ratio Vertical (62/38)",
    28: "Golden Ratio Horizontal (62/38)",
    29: "Uneven Triple Vertical (50/25/25)",
    30: "Uneven Triple Horizontal (20/60/20)",
    
    # Diagonal & Dynamic (31-45)
    31: "Diagonal Cascade (Top-Left to Bottom-Right)",
    32: "Diagonal Cascade (Top-Right to Bottom-Left)",
    33: "Diagonal Cascade (Bottom-Left to Top-Right)",
    34: "Diagonal Cascade (Bottom-Right to Top-Left)",
    35: "Cross-Diagonal (X-Pattern)",
    36: "Chevron Up",
    37: "Chevron Down",
    38: "Lightning Bolt",
    39: "Waterfall Flow",
    40: "Ascending Stairs",
    41: "Wave Pattern",
    42: "Mountain Peak",
    43: "Valley Dip",
    44: "Spiral Diagonal",
    45: "Ribbon Twist",
    
    # Circular & Radial (46-60)
    46: "Circular Orbit (Clockwise)",
    47: "Circular Orbit (Counter-Clockwise)",
    48: "Elliptical Orbit",
    49: "Double Orbit",
    50: "Radial Expansion (Outward)",
    51: "Radial Contraction (Inward)",
    52: "Compass Points (4 Directions)",
    53: "Compass Points (8 Directions)",
    54: "Sunburst Radial",
    55: "Target Circles (Concentric)",
    56: "Semicircle Arc (Top)",
    57: "Semicircle Arc (Bottom)",
    58: "Quarter Circle (Top-Right)",
    59: "Quarter Circle (Bottom-Left)",
    60: "Spiral (Inward)",
    
    # Grid & Structured (61-75)
    61: "Four-Quadrant (Equal)",
    62: "Four-Quadrant (Unequal)",
    63: "Six-Grid (2×3)",
    64: "Six-Grid (3×2)",
    65: "Nine-Grid (3×3)",
    66: "Checkerboard Pattern",
    67: "Brick Pattern (Offset Grid)",
    68: "Honeycomb Grid",
    69: "Plus/Cross Grid",
    70: "L-Shaped Grid",
    71: "T-Shaped Grid",
    72: "U-Shaped Grid",
    73: "Border Frame Grid",
    74: "Scattered Grid",
    75: "Nested Squares",
    
    # Comparison & Contrast (76-85)
    76: "Before/After (Left/Right)",
    77: "Before/After (Top/Bottom)",
    78: "Before/After (Diagonal Split)",
    79: "Problem/Solution Split",
    80: "Old vs New",
    81: "Small vs Large (Scale Contrast)",
    82: "Simple vs Complex",
    83: "Empty vs Full",
    84: "Light vs Dark (Value Contrast)",
    85: "Few vs Many",
    
    # Specialty & Advanced (86-100)
    86: "Timeline Journey (Horizontal)",
    87: "Timeline Journey (Vertical)",
    88: "Timeline Journey (Spiral)",
    89: "Hub-and-Spoke",
    90: "Tree/Branch Structure",
    91: "River Delta",
    92: "Funnel (Wide to Narrow)",
    93: "Inverse Funnel (Narrow to Wide)",
    94: "Pinwheel",
    95: "Overlapping Circles (Venn)",
    96: "Scattered Constellation",
    97: "Magazine Layout",
    98: "Layered Depth (Front-to-Back)",
    99: "Woven Pattern",
    100: "Floating Islands",
}


# Category definitions
CATEGORIES = {
    "asymmetric": list(range(1, 16)),
    "split": list(range(16, 31)),
    "diagonal": list(range(31, 46)),
    "circular": list(range(46, 61)),
    "grid": list(range(61, 76)),
    "comparison": list(range(76, 86)),
    "specialty": list(range(86, 101)),
}


# Scene type recommendations
SCENE_TYPE_RECOMMENDATIONS = {
    "opening": [46, 50, 51, 60, 89, 95],
    "closing": [46, 50, 51, 60, 89, 95, 100],
    "problem": [1, 2, 46, 76, 77, 83],
    "discovery": [31, 33, 50, 56, 92, 96],
    "solution": [17, 61, 70, 89, 90, 93],
    "impact": [42, 50, 86, 87, 91, 100],
    "comparison": [76, 77, 78, 79, 80, 81, 82, 83, 84, 85],
    "timeline": [86, 87, 88],
    "network": [89, 90, 91, 95],
}


# Visual weight classification
VISUAL_WEIGHT = {
    "light": [2, 7, 14, 19, 24, 56, 73, 83, 96, 100],
    "medium": [16, 21, 25, 51, 61, 65, 76, 86, 89, 95],
    "heavy": [1, 9, 48, 49, 62, 66, 74, 90, 97, 99],
}


def get_category(pattern_id: int) -> str:
    """Get the category name for a pattern ID"""
    for category, ids in CATEGORIES.items():
        if pattern_id in ids:
            return category
    return "unknown"


def suggest_patterns(
    scene_type: Optional[str] = None,
    used_patterns: Optional[List[int]] = None,
    previous_pattern: Optional[int] = None,
    count: int = 5
) -> List[Dict[str, any]]:
    """
    Suggest optimal layout patterns based on context
    
    Args:
        scene_type: Type of scene (opening, problem, solution, etc.)
        used_patterns: List of pattern IDs already used
        previous_pattern: The pattern ID used in the previous scene
        count: Number of suggestions to return
    
    Returns:
        List of dicts with pattern_id, name, category, reason
    """
    used_patterns = used_patterns or []
    
    # Start with scene type recommendations if provided
    if scene_type and scene_type in SCENE_TYPE_RECOMMENDATIONS:
        candidates = SCENE_TYPE_RECOMMENDATIONS[scene_type].copy()
    else:
        candidates = list(LAYOUT_PATTERNS.keys())
    
    # Remove already used patterns
    candidates = [p for p in candidates if p not in used_patterns]
    
    # If previous pattern provided, avoid same category
    if previous_pattern:
        prev_category = get_category(previous_pattern)
        # Keep some from same category but deprioritize
        same_category = [p for p in candidates if get_category(p) == prev_category]
        diff_category = [p for p in candidates if get_category(p) != prev_category]
        
        # Prefer different categories (80% chance)
        if diff_category and random.random() < 0.8:
            candidates = diff_category
        else:
            candidates = same_category + diff_category
    
    # If we don't have enough candidates, add from unused patterns
    if len(candidates) < count:
        unused = [p for p in LAYOUT_PATTERNS.keys() if p not in used_patterns]
        candidates.extend(unused[:count - len(candidates)])
    
    # Randomly select from candidates
    selected = random.sample(candidates, min(count, len(candidates)))
    
    # Build suggestions with metadata
    suggestions = []
    for pattern_id in selected:
        category = get_category(pattern_id)
        
        # Determine weight
        weight = "medium"
        for w, ids in VISUAL_WEIGHT.items():
            if pattern_id in ids:
                weight = w
                break
        
        # Determine reason
        reason_parts = []
        if scene_type and pattern_id in SCENE_TYPE_RECOMMENDATIONS.get(scene_type, []):
            reason_parts.append(f"Recommended for {scene_type} scenes")
        if previous_pattern and get_category(pattern_id) != get_category(previous_pattern):
            reason_parts.append("Different category from previous")
        reason_parts.append(f"{weight.capitalize()} visual weight")
        
        suggestions.append({
            "pattern_id": pattern_id,
            "name": LAYOUT_PATTERNS[pattern_id],
            "category": category,
            "weight": weight,
            "reason": " | ".join(reason_parts)
        })
    
    return suggestions


def generate_sequence(num_scenes: int, scene_types: Optional[List[str]] = None) -> List[Dict]:
    """
    Generate a complete non-repeating pattern sequence for an explainer
    
    Args:
        num_scenes: Number of scenes in the explainer
        scene_types: Optional list of scene types (must match num_scenes)
    
    Returns:
        List of dicts with scene_number, pattern_id, name, category
    """
    if scene_types and len(scene_types) != num_scenes:
        raise ValueError("scene_types length must match num_scenes")
    
    sequence = []
    used_patterns = []
    previous_pattern = None
    
    for i in range(num_scenes):
        scene_type = scene_types[i] if scene_types else None
        
        # Get suggestions
        suggestions = suggest_patterns(
            scene_type=scene_type,
            used_patterns=used_patterns,
            previous_pattern=previous_pattern,
            count=3
        )
        
        # Pick the first suggestion
        if suggestions:
            selected = suggestions[0]
            sequence.append({
                "scene_number": i,
                "pattern_id": selected["pattern_id"],
                "name": selected["name"],
                "category": selected["category"],
                "weight": selected["weight"]
            })
            used_patterns.append(selected["pattern_id"])
            previous_pattern = selected["pattern_id"]
    
    return sequence


def save_sequence(sequence: List[Dict], output_path: Path):
    """Save pattern sequence to JSON file"""
    with open(output_path, 'w') as f:
        json.dump(sequence, f, indent=2)


def load_sequence(input_path: Path) -> List[Dict]:
    """Load pattern sequence from JSON file"""
    with open(input_path, 'r') as f:
        return json.load(f)


def print_suggestions(suggestions: List[Dict]):
    """Pretty print pattern suggestions"""
    print("\n" + "="*70)
    print("LAYOUT PATTERN SUGGESTIONS")
    print("="*70)
    
    for i, s in enumerate(suggestions, 1):
        print(f"\n{i}. Pattern #{s['pattern_id']}: {s['name']}")
        print(f"   Category: {s['category'].capitalize()}")
        print(f"   Weight: {s['weight'].capitalize()}")
        print(f"   Reason: {s['reason']}")


def print_sequence(sequence: List[Dict]):
    """Pretty print pattern sequence"""
    print("\n" + "="*70)
    print("LAYOUT PATTERN SEQUENCE")
    print("="*70)
    
    for item in sequence:
        print(f"\nScene {item['scene_number']:2d}: Pattern #{item['pattern_id']:3d} - {item['name']}")
        print(f"           Category: {item['category'].capitalize():15s} | Weight: {item['weight'].capitalize()}")


def main():
    """Command-line interface"""
    import argparse
    
    parser = argparse.ArgumentParser(
        description='Intelligent layout pattern selector',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Get suggestions for a problem scene
  python layout_selector.py --suggest --type problem
  
  # Get suggestions avoiding pattern #46
  python layout_selector.py --suggest --previous 46
  
  # Generate sequence for 12-scene explainer
  python layout_selector.py --generate 12
  
  # Generate sequence with scene types
  python layout_selector.py --generate 12 --types opening problem problem discovery solution solution impact impact solution problem solution closing
        """
    )
    
    parser.add_argument(
        '--suggest',
        action='store_true',
        help='Get pattern suggestions'
    )
    
    parser.add_argument(
        '--generate',
        type=int,
        metavar='N',
        help='Generate complete sequence for N scenes'
    )
    
    parser.add_argument(
        '--type',
        choices=list(SCENE_TYPE_RECOMMENDATIONS.keys()),
        help='Scene type for suggestions'
    )
    
    parser.add_argument(
        '--types',
        nargs='+',
        help='Scene types for sequence generation (space-separated)'
    )
    
    parser.add_argument(
        '--previous',
        type=int,
        metavar='ID',
        help='Previous pattern ID to avoid similar patterns'
    )
    
    parser.add_argument(
        '--used',
        type=int,
        nargs='+',
        metavar='ID',
        help='Already used pattern IDs'
    )
    
    parser.add_argument(
        '--count',
        type=int,
        default=5,
        help='Number of suggestions (default: 5)'
    )
    
    parser.add_argument(
        '--output',
        type=Path,
        help='Save sequence to JSON file'
    )
    
    args = parser.parse_args()
    
    if args.suggest:
        # Get suggestions
        suggestions = suggest_patterns(
            scene_type=args.type,
            used_patterns=args.used,
            previous_pattern=args.previous,
            count=args.count
        )
        print_suggestions(suggestions)
    
    elif args.generate:
        # Generate sequence
        sequence = generate_sequence(args.generate, args.types)
        print_sequence(sequence)
        
        if args.output:
            save_sequence(sequence, args.output)
            print(f"\n✓ Sequence saved to: {args.output}")
    
    else:
        parser.print_help()


if __name__ == "__main__":
    main()


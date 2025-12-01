"""
Unit tests for layout_selector.py
"""
import pytest
from scripts.layout_selector import (
    suggest_patterns,
    generate_sequence,
    get_category,
    LAYOUT_PATTERNS,
    CATEGORIES
)


def test_suggest_patterns_basic():
    """Test basic pattern suggestions"""
    suggestions = suggest_patterns(
        scene_type="problem",
        used_patterns=[],
        previous_pattern=None,
        count=5
    )
    
    assert isinstance(suggestions, list)
    assert len(suggestions) == 5
    
    for suggestion in suggestions:
        assert 'pattern_id' in suggestion
        assert 'name' in suggestion
        assert 'category' in suggestion
        assert 'weight' in suggestion
        assert 'reason' in suggestion
        assert isinstance(suggestion['pattern_id'], int)
        assert 1 <= suggestion['pattern_id'] <= 100


def test_suggest_patterns_excludes_used():
    """Test that used patterns are excluded"""
    used = [1, 2, 3, 4, 5]
    suggestions = suggest_patterns(
        scene_type="problem",
        used_patterns=used,
        previous_pattern=None,
        count=10
    )
    
    suggested_ids = [s['pattern_id'] for s in suggestions]
    for used_id in used:
        assert used_id not in suggested_ids


def test_generate_sequence_basic():
    """Test basic sequence generation"""
    sequence = generate_sequence(12)
    
    assert isinstance(sequence, list)
    assert len(sequence) == 12
    
    for item in sequence:
        assert 'scene_number' in item
        assert 'pattern_id' in item
        assert 'name' in item
        assert 'category' in item
        assert 'weight' in item


def test_generate_sequence_no_repeats():
    """Test that sequence has no repeated patterns"""
    sequence = generate_sequence(12)
    
    pattern_ids = [item['pattern_id'] for item in sequence]
    assert len(pattern_ids) == len(set(pattern_ids))  # No duplicates


def test_generate_sequence_with_types():
    """Test sequence generation with scene types"""
    scene_types = ["opening", "problem", "problem", "discovery", "solution"] * 2 + ["solution", "closing"]
    sequence = generate_sequence(12, scene_types)
    
    assert len(sequence) == 12
    assert len(sequence) == len(scene_types)


def test_get_category_valid():
    """Test getting category for valid pattern ID"""
    category = get_category(1)
    
    assert isinstance(category, str)
    assert category in CATEGORIES.keys()


def test_get_category_invalid():
    """Test getting category for invalid pattern ID"""
    # Pattern IDs should be 1-100, but function returns "unknown" for invalid IDs
    assert get_category(0) == "unknown"
    assert get_category(101) == "unknown"


def test_layout_patterns_complete():
    """Test that all patterns 1-100 exist"""
    for pattern_id in range(1, 101):
        assert pattern_id in LAYOUT_PATTERNS
        assert isinstance(LAYOUT_PATTERNS[pattern_id], str)
        assert len(LAYOUT_PATTERNS[pattern_id]) > 0


def test_categories_complete():
    """Test that categories contain valid pattern IDs"""
    all_category_ids = []
    for category, pattern_ids in CATEGORIES.items():
        assert isinstance(category, str)
        assert isinstance(pattern_ids, list)
        assert len(pattern_ids) > 0
        all_category_ids.extend(pattern_ids)
    
    # All pattern IDs in categories should be 1-100
    for pattern_id in all_category_ids:
        assert 1 <= pattern_id <= 100


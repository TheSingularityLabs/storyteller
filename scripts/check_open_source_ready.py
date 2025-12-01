#!/usr/bin/env python3
"""
Security check script to verify codebase is ready for open source.

This script checks for:
- API keys and secrets
- Hardcoded credentials
- Proprietary identifiers
- Sensitive file paths
"""

import os
import re
from pathlib import Path
from typing import List, Tuple

# Patterns to search for
SENSITIVE_PATTERNS = [
    (r'API_KEY\s*=\s*["\'][^"\']+["\']', 'Hardcoded API key'),
    (r'FAL_KEY\s*=\s*["\'][^"\']+["\']', 'Hardcoded FAL key'),
    (r'ELEVENLABS_API_KEY\s*=\s*["\'][^"\']+["\']', 'Hardcoded ElevenLabs key'),
    (r'B7MDFzV4AOf19yty4RcE', 'Custom voice ID exposed'),
    (r'secret\s*=\s*["\'][^"\']+["\']', 'Hardcoded secret'),
    (r'password\s*=\s*["\'][^"\']+["\']', 'Hardcoded password'),
    (r'token\s*=\s*["\'][^"\']+["\']', 'Hardcoded token'),
]

# Files/directories to exclude from search
EXCLUDE_PATTERNS = [
    '__pycache__',
    '.git',
    'output',
    'archive',
    'scripts_to_process',
    '.venv',
    'venv',
    'node_modules',
    'check_open_source_ready.py',  # Don't check this file
]

# File extensions to check
CHECK_EXTENSIONS = ['.py', '.md', '.txt', '.yaml', '.yml', '.json']


def should_exclude_file(filepath: Path) -> bool:
    """Check if file should be excluded from scanning."""
    path_str = str(filepath)
    return any(exclude in path_str for exclude in EXCLUDE_PATTERNS)


def check_file(filepath: Path) -> List[Tuple[str, int, str]]:
    """
    Check a single file for sensitive patterns.
    
    Returns:
        List of (pattern_name, line_number, line_content) tuples
    """
    issues = []
    
    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            for line_num, line in enumerate(f, 1):
                for pattern, pattern_name in SENSITIVE_PATTERNS:
                    if re.search(pattern, line, re.IGNORECASE):
                        issues.append((pattern_name, line_num, line.strip()))
    except Exception as e:
        print(f"⚠️  Error reading {filepath}: {e}")
    
    return issues


def scan_directory(root_dir: Path) -> dict:
    """Scan directory for sensitive content."""
    all_issues = {}
    
    for filepath in root_dir.rglob('*'):
        if should_exclude_file(filepath):
            continue
        
        if filepath.is_file() and filepath.suffix in CHECK_EXTENSIONS:
            issues = check_file(filepath)
            if issues:
                all_issues[str(filepath)] = issues
    
    return all_issues


def main():
    """Main function to run security check."""
    root_dir = Path(__file__).parent.parent
    
    print("🔍 Scanning codebase for sensitive content...")
    print("=" * 60)
    
    issues = scan_directory(root_dir)
    
    if not issues:
        print("✅ No sensitive content found!")
        print("\nYour codebase appears ready for open source.")
        return 0
    
    print(f"\n⚠️  Found {len(issues)} file(s) with potential issues:\n")
    
    total_issues = 0
    for filepath, file_issues in issues.items():
        print(f"📄 {filepath}")
        for pattern_name, line_num, line_content in file_issues:
            print(f"   Line {line_num}: {pattern_name}")
            print(f"   Content: {line_content[:80]}...")
            total_issues += 1
        print()
    
    print("=" * 60)
    print(f"❌ Found {total_issues} issue(s) that need to be addressed.")
    print("\nRecommendations:")
    print("1. Remove hardcoded API keys (use environment variables)")
    print("2. Remove custom voice IDs (use config.example.py)")
    print("3. Review all flagged files before publishing")
    print("\nSee OPEN_SOURCE_PREPARATION.md for detailed guidance.")
    
    return 1


if __name__ == "__main__":
    exit(main())


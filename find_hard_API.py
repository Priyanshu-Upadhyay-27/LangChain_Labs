#!/usr/bin/env python3
"""
Script to find potential hardcoded API keys in Python files
"""
import os
import re
from pathlib import Path

# Common patterns for API keys
API_KEY_PATTERNS = [
    r'["\']?api_key["\']?\s*[=:]\s*["\'][^"\']+["\']',
    r'["\']?API_KEY["\']?\s*[=:]\s*["\'][^"\']+["\']',
    r'["\']?openai_api_key["\']?\s*[=:]\s*["\'][^"\']+["\']',
    r'["\']?OPENAI_API_KEY["\']?\s*[=:]\s*["\'][^"\']+["\']',
    r'["\']?secret["\']?\s*[=:]\s*["\'][^"\']+["\']',
    r'["\']?SECRET["\']?\s*[=:]\s*["\'][^"\']+["\']',
    r'sk-[a-zA-Z0-9]{48}',  # OpenAI API key pattern
    r'sk-[a-zA-Z0-9]{32}T3BlbkFJ[a-zA-Z0-9]{20}',  # OpenAI API key pattern (newer)
    r'gsk_[a-zA-Z0-9]{52}',  # Google API key pattern
    r'AIza[0-9A-Za-z_\-]{35}',  # Google API key pattern
]


def find_api_keys_in_file(file_path):
    """Find potential API keys in a single file"""
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()

        found_keys = []
        for i, line in enumerate(content.split('\n'), 1):
            for pattern in API_KEY_PATTERNS:
                matches = re.findall(pattern, line, re.IGNORECASE)
                if matches:
                    found_keys.append({
                        'line_number': i,
                        'line_content': line.strip(),
                        'matches': matches
                    })
        return found_keys
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return []


def scan_directory(directory_path):
    """Scan directory for Python files with potential API keys"""
    results = {}

    for root, dirs, files in os.walk(directory_path):
        # Skip virtual environment and cache directories
        dirs[:] = [d for d in dirs if d not in ['.venv', '__pycache__', '.git']]

        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                api_keys = find_api_keys_in_file(file_path)
                if api_keys:
                    results[file_path] = api_keys

    return results


def main():
    project_dir = "."  # Current directory
    print("🔍 Scanning for potential API keys in Python files...")
    print("=" * 60)

    results = scan_directory(project_dir)

    if not results:
        print("✅ No potential API keys found in Python files!")
        return

    print(f"⚠️  Found potential API keys in {len(results)} files:")
    print()

    for file_path, api_keys in results.items():
        print(f"📄 File: {file_path}")
        for key_info in api_keys:
            print(f"   Line {key_info['line_number']}: {key_info['line_content']}")
        print()

    print("🔧 Next steps:")
    print("1. Review the files listed above")
    print("2. Move hardcoded API keys to .env files")
    print("3. Use os.getenv() or python-dotenv to load environment variables")
    print("4. Add .env to your .gitignore file")


if __name__ == "__main__":
    main()
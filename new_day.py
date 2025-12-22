#!/usr/bin/env python3
"""
Helper script to create a new day directory with template files.
Usage: python new_day.py <day_number>
"""

import sys
from pathlib import Path
from shutil import copy


def create_day(day: int):
    """Create a new day directory with template files."""
    day_str = f"day{day:02d}"
    day_dir = Path(day_str)
    
    if day_dir.exists():
        print(f"Error: {day_str} already exists!")
        return False
    
    # Create directory
    day_dir.mkdir(parents=True, exist_ok=True)
    
    # Copy template to solution.py
    template = Path("template.py")
    if template.exists():
        copy(template, day_dir / "solution.py")
        # Update the day number in the solution file
        solution_file = day_dir / "solution.py"
        content = solution_file.read_text()
        content = content.replace("Day XX", f"Day {day:02d}")
        content = content.replace("day=1", f"day={day}")
        solution_file.write_text(content)
    
    # Create empty input files
    (day_dir / "input.txt").write_text("# Paste your puzzle input here\n")
    (day_dir / "test_input.txt").write_text("# Paste test input here (optional)\n")
    
    print(f"Created {day_str}/ directory with template files!")
    print(f"  - {day_str}/solution.py")
    print(f"  - {day_str}/input.txt")
    print(f"  - {day_str}/test_input.txt")
    
    return True


def main():
    if len(sys.argv) != 2:
        print("Usage: python new_day.py <day_number>")
        print("Example: python new_day.py 2")
        sys.exit(1)
    
    try:
        day = int(sys.argv[1])
        if not (1 <= day <= 25):
            print("Error: Day number must be between 1 and 25")
            sys.exit(1)
        
        create_day(day)
    except ValueError:
        print("Error: Day number must be an integer")
        sys.exit(1)


if __name__ == "__main__":
    main()


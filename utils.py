"""
Utility functions for Advent of Code problems.
"""

from pathlib import Path
from typing import List, Optional


def read_input(day: int, filename: str = "input.txt") -> List[str]:
    """
    Read input file for a given day.
    
    Args:
        day: Day number (1-25)
        filename: Name of the input file (default: "input.txt")
    
    Returns:
        List of lines from the input file
    """
    day_dir = Path(f"day{day:02d}")
    input_file = day_dir / filename
    
    if not input_file.exists():
        raise FileNotFoundError(f"Input file not found: {input_file}")
    
    with open(input_file, "r") as f:
        return [line.rstrip("\n") for line in f.readlines()]


def read_input_raw(day: int, filename: str = "input.txt") -> str:
    """
    Read input file as raw text for a given day.
    
    Args:
        day: Day number (1-25)
        filename: Name of the input file (default: "input.txt")
    
    Returns:
        Raw text content of the input file
    """
    day_dir = Path(f"day{day:02d}")
    input_file = day_dir / filename
    
    if not input_file.exists():
        raise FileNotFoundError(f"Input file not found: {input_file}")
    
    with open(input_file, "r") as f:
        return f.read().rstrip("\n")


def read_input_lines(day: int, filename: str = "input.txt", strip: bool = True) -> List[str]:
    """
    Read input file and return lines.
    
    Args:
        day: Day number (1-25)
        filename: Name of the input file (default: "input.txt")
        strip: Whether to strip whitespace from lines (default: True)
    
    Returns:
        List of lines from the input file
    """
    lines = read_input(day, filename)
    if strip:
        return [line.strip() for line in lines if line.strip()]
    return lines


def parse_ints(line: str) -> List[int]:
    """
    Parse all integers from a line.
    
    Args:
        line: Input line containing integers
    
    Returns:
        List of integers found in the line
    """
    import re
    return [int(x) for x in re.findall(r"-?\d+", line)]


def parse_grid(lines: List[str], converter: Optional[callable] = None) -> List[List]:
    """
    Parse a grid from input lines.
    
    Args:
        lines: List of input lines
        converter: Optional function to convert each character (default: None, returns as-is)
    
    Returns:
        2D grid as list of lists
    """
    if converter is None:
        converter = lambda x: x
    
    return [[converter(c) for c in line] for line in lines]


def manhattan_distance(x1: int, y1: int, x2: int, y2: int) -> int:
    """
    Calculate Manhattan distance between two points.
    
    Args:
        x1, y1: Coordinates of first point
        x2, y2: Coordinates of second point
    
    Returns:
        Manhattan distance
    """
    return abs(x1 - x2) + abs(y1 - y2)


def neighbors_4(x: int, y: int, max_x: Optional[int] = None, max_y: Optional[int] = None) -> List[tuple]:
    """
    Get 4-directional neighbors (up, down, left, right).
    
    Args:
        x, y: Current coordinates
        max_x, max_y: Optional bounds (exclusive)
    
    Returns:
        List of (x, y) tuples for valid neighbors
    """
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    neighbors = []
    
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if max_x is None or (0 <= nx < max_x):
            if max_y is None or (0 <= ny < max_y):
                neighbors.append((nx, ny))
    
    return neighbors


def neighbors_8(x: int, y: int, max_x: Optional[int] = None, max_y: Optional[int] = None) -> List[tuple]:
    """
    Get 8-directional neighbors (including diagonals).
    
    Args:
        x, y: Current coordinates
        max_x, max_y: Optional bounds (exclusive)
    
    Returns:
        List of (x, y) tuples for valid neighbors
    """
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    neighbors = []
    
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if max_x is None or (0 <= nx < max_x):
            if max_y is None or (0 <= ny < max_y):
                neighbors.append((nx, ny))
    
    return neighbors


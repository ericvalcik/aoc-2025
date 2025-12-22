"""
Advent of Code 2025 - Day XX Template

Copy this file to dayXX/solution.py and fill in your solution.
"""

from utils import read_input, read_input_raw


def part1(data):
    """
    Solve part 1 of the problem.
    
    Args:
        data: Input data (list of lines or raw string)
    
    Returns:
        Solution to part 1
    """
    # TODO: Implement part 1
    pass


def part2(data):
    """
    Solve part 2 of the problem.
    
    Args:
        data: Input data (list of lines or raw string)
    
    Returns:
        Solution to part 2
    """
    # TODO: Implement part 2
    pass


def main():
    # Read input
    # For line-by-line input:
    # data = read_input(day=1)
    
    # For raw text input:
    # data = read_input_raw(day=1)
    
    # Example with test input:
    # data = read_input(day=1, filename="test_input.txt")
    
    data = read_input(day=1)
    
    # Solve
    result1 = part1(data)
    print(f"Part 1: {result1}")
    
    result2 = part2(data)
    print(f"Part 2: {result2}")


if __name__ == "__main__":
    main()


"""
Advent of Code 2025 - Day 01

Copy from template.py and implement your solution here.
"""

import sys
from pathlib import Path

# Add parent directory to path to import utils
sys.path.insert(0, str(Path(__file__).parent.parent))

from utils import read_input, read_input_raw


def part1(data):
    x = 50
    total_zeroes = 0
    for line in data:
        if line[0] == 'L':
            x = (x - int(line[1:])) % 100
        else:
            x = (x + int(line[1:])) % 100
        if x == 0:
            total_zeroes += 1
    return total_zeroes


def part2(data):
    x = 50
    total_zero_passed = 0
    # print(data)
    for line in data:
        # print(line)
        if line[0] == 'L':
            num = int(line[1:])
            if x - num <= 0:
                total_zero_passed += (1 if x != 0 else 0) + abs(x - num) // 100
            x = (x - num) % 100
        else:
            num = int(line[1:])
            total_zero_passed += (x + num) // 100
            x = (x + num) % 100
    #    print(f"x: {x}, total_zero_passed: {total_zero_passed}")
    return total_zero_passed


def main():
    # Read input
    data = read_input(day=1, filename="input.txt")
    
    # Solve
    result1 = part1(data)
    print(f"Part 1: {result1}")
    
    result2 = part2(data)
    print(f"Part 2: {result2}")


if __name__ == "__main__":
    main()


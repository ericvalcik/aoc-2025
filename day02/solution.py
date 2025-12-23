import sys
from pathlib import Path

# Add parent directory to path to import utils
sys.path.insert(0, str(Path(__file__).parent.parent))

from utils import read_input


def has_pattern(x: str, pattern: str) -> bool:
    if len(x) % len(pattern) != 0:
        return False

    for i in range(len(pattern), len(x), len(pattern)):
        if x[i:i+len(pattern)] != pattern:
            return False
    return True


def part1(data: str):
    result = 0
    ranges = data.split(",")
    for range_str in ranges:
        start, end = range_str.split("-")
        start_num = int(start)
        end_num = int(end)
        for num in range(start_num, end_num + 1):
            x = str(num)
            if (len(x) % 2 == 0) and (x[:len(x)//2] == x[len(x)//2:]):
                result += num
    return result


def part2(data):
    result = 0
    ranges = data.split(",")
    for range_str in ranges:
        start, end = range_str.split("-")
        start_num = int(start)
        end_num = int(end)
        for num in range(start_num, end_num + 1):
            x = str(num)
            for i in range(1, len(x) // 2 + 1):
                pattern = x[:i]
                if has_pattern(x, pattern):
                    result += num
                    break
    return result


def run_tests():
    print('running tests')
    print(f'has_pattern("1234567890", "1234") -> {has_pattern("1234567890", "1234")}')
    print(f'has_pattern("12341234", "1234") -> {has_pattern("12341234", "1234")}')
    print(f'has_pattern("11111", "1") -> {has_pattern("11111", "1")}')
    print(f'has_pattern("1212121212", "12") -> {has_pattern("1212121212", "12")}')
    print(f'has_pattern("1212121212", "13") -> {has_pattern("1212121212", "13")}')
    print(f'has_pattern("1212121212", "3") -> {has_pattern("1212121212", "3")}')
    print(f'has_pattern("1212121212", "1") -> {has_pattern("1212121212", "1")}')
    print(f'has_pattern("1212121212", "1212") -> {has_pattern("1212121212", "1212")}')


def main():
    data = read_input(day=2, filename="input.txt")[0]
    # run_tests()

    # Solve
    result1 = part1(data)
    print(f"Part 1: {result1}")
    
    result2 = part2(data)
    print(f"Part 2: {result2}")


if __name__ == "__main__":
    main()


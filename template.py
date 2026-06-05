import argparse
import sys
from pathlib import Path

# Add parent directory to path to import utils
sys.path.insert(0, str(Path(__file__).parent.parent))

from utils import read_input


def part1(data):
    pass


def part2(data):
    pass


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--test",
        action="store_true",
        help="Use test_input.txt instead of input.txt",
    )
    parser.add_argument(
        "--part1",
        action="store_true",
        help="Run only part 1",
    )
    parser.add_argument(
        "--part2",
        action="store_true",
        help="Run only part 2",
    )
    args = parser.parse_args()

    filename = "test_input.txt" if args.test else "input.txt"
    data = read_input(day=1, filename=filename)

    run_all = not args.part1 and not args.part2

    if run_all or args.part1:
        result1 = part1(data)
        print(f"Part 1: {result1}")

    if run_all or args.part2:
        result2 = part2(data)
        print(f"Part 2: {result2}")


if __name__ == "__main__":
    main()


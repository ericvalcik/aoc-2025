import argparse
import sys
from pathlib import Path

# Add parent directory to path to import utils
sys.path.insert(0, str(Path(__file__).parent.parent))

from utils import read_input


def part1(data):
    sum = 0
    for line in data:
        first_digit = -1
        first_digit_index = -1
        for index, char in enumerate(line[:-1]):
            digit = int(char)
            if digit > first_digit:
                first_digit = digit 
                first_digit_index = index

        second_digit = -1
        for char in line[first_digit_index+1:]:
            digit = int(char)
            if digit > second_digit:
                second_digit = digit
        sum += first_digit * 10 + second_digit
    return sum


def part2(data):
    NO_OF_DIGITS = 12

    sum = 0
    for line_index, line in enumerate(data):
        print(f'line {line_index+1} {line}\n')
        line_sum = 0
        index = 0
        for i in range(NO_OF_DIGITS):
            line_sum *= 10
            digit = -1
            inner_index = -1
            offset = i + 1 - NO_OF_DIGITS

            if (offset == 0):
                offset = len(line)

            for curr_index, char in enumerate(line[index:offset]):
                curr = int(char)
                if curr > digit:
                    digit = curr 
                    inner_index = curr_index
            line_sum += digit
            index += inner_index + 1
            print(f'digit {i+1}: {digit}, index: {index}')
        print(f'\nline {line_index+1}, line sum {line_sum}\n')
        sum += line_sum

    return sum


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
    data = read_input(day=3, filename=filename)

    run_all = not args.part1 and not args.part2

    if run_all or args.part1:
        result1 = part1(data)
        print(f"Part 1: {result1}")

    if run_all or args.part2:
        result2 = part2(data)
        print(f"Part 2: {result2}")


if __name__ == "__main__":
    main()


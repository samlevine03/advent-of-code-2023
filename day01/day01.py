# https://adventofcode.com/2023/day/01

from utils import get_input
import re

# Part 1

def extract_first_last_digits(string):
    digits = re.findall(r'\d', string)
    return int(digits[0] + digits[-1]) if digits else 0

# Part 2

def replace_spelled_numbers(word):
    num_map = {
        'one': '1', 'two': '2', 'three': '3', 'four': '4',
        'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'
    }
    
    pattern = re.compile('|'.join(num_map.keys()))
    return pattern.sub(lambda x: num_map[x.group()], word)

# -------- MAIN FUNCTION -------- #
def main():
    lines = get_input()

    part1 = sum(extract_first_last_digits(line) for line in lines)
    print(f"Part 1: {part1}")

    converted_lines = [replace_spelled_numbers(line) for line in lines]
    part2 = sum(extract_first_last_digits(line) for line in converted_lines)
    print(f"Part 2: {part2}")

if __name__ == "__main__":
    main()

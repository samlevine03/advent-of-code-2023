# https://adventofcode.com/2023/day/12

from utils import get_input

# Part 1

def num_combos(line):
    # working: .
    # damaged: #
    # unknown: ?
    conditions, nums = line
    if conditions.count('.') >= len(nums) - 1:
        conditions = conditions.split('.')

# Part 2



# -------- MAIN FUNCTION -------- #
def main():
    lines = get_input()
    example_lines = [
        "#.#.### 1,1,3",
        ".#...#....###. 1,1,3",
        ".#.###.#.###### 1,3,1,6",
        "####.#...#... 4,1,1",
        "#....######..#####. 1,6,5",
        ".###.##....# 3,2,1",
    ]

    

    pass

if __name__ == "__main__":
    main()

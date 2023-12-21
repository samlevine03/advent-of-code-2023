# https://adventofcode.com/2023/day/09

from utils import get_input

# Part 1

def extrapolate(nums):
    diffs = [nums[i+1] - nums[i] for i in range(len(nums) - 1)]
    last_diff_list = [nums[-1]]
    while any(diffs):
        last_diff_list.append(diffs[-1])
        diffs = [diffs[i+1] - diffs[i] for i in range(len(diffs) - 1)]
    return sum(last_diff_list)

# Part 2



# -------- MAIN FUNCTION -------- #
def main():
    lines = get_input()
    total = sum([extrapolate([int(n) for n in line.split()]) for line in lines])
    print(f"Part 1: {total}")
    
    total = sum([extrapolate([int(n) for n in line.split()][::-1]) for line in lines])
    print(f"Part 2: {total}")

if __name__ == "__main__":
    main()

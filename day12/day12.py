# https://adventofcode.com/2023/day/12

from utils import get_input

# Part 1

def num_combos(conditions, nums):
    # had to do a good bit of research (shoutout reddit) to 
    # figure this one out without needing DP

    # base cases
    # empty conditions only works if we have no nums
    if conditions == "":
        return 1 if len(nums) == 0 else 0
    
    # empty nums only works if we have no damaged conditions
    if len(nums) == 0:
        return 0 if '#' in conditions else 1
    
    # recursive cases?
    res = 0

    # If the first spring is operational or unknown ('.' or '?'), 
    # recursively call the function with the rest of the springs 
    # keeping nums unchanged.
    if conditions[0] in ".?":
        res += num_combos(conditions[1:], nums)

    # If the first spring is broken or unknown ('#' or '?'), and 
    # the first number in nums matches the length of the broken 
    # group in conditions, recursively call the function with the 
    # remaining conditions after the broken group and the rest of the numbers.
    if conditions[0] in "#?":
        if (nums[0] <= len(conditions)) and ("." not in conditions[:nums[0]]) and (nums[0] == len(conditions) or conditions[nums[0]] != "#"):
            res += num_combos(conditions[nums[0] + 1:], nums[1:])

    return res

# Part 2

def num_combos_unfolded(conditions, nums, memo):
    if conditions == "":
        return 1 if len(nums) == 0 else 0
    
    if len(nums) == 0:
        return 0 if '#' in conditions else 1
    
    if (conditions, nums) in memo:
        return memo[(conditions, nums)]
    
    res = 0
    if conditions[0] in ".?":
        res += num_combos_unfolded(conditions[1:], nums, memo)

    if conditions[0] in "#?":
        if (nums[0] <= len(conditions)) and ("." not in conditions[:nums[0]]) and (nums[0] == len(conditions) or conditions[nums[0]] != "#"):
            res += num_combos_unfolded(conditions[nums[0] + 1:], nums[1:], memo)

    memo[(conditions, nums)] = res
    return res

# -------- MAIN FUNCTION -------- #
def main():
    lines = get_input()
    total = 0
    for line in lines:
        conditions, nums = line.split()
        nums = list(map(int, nums.split(",")))
        total += num_combos(conditions, nums)

    print(f"Part 1: {total}")
    
    memo = {}
    total = 0
    for line in lines:
        conditions, nums = line.split()
        conditions = '?'.join([conditions] * 5)
        nums = tuple(map(int, nums.split(",")))
        nums *= 5
        total += num_combos_unfolded(conditions, nums, memo)

    print(f"Part 2: {total}")

    pass

if __name__ == "__main__":
    main()

# https://adventofcode.com/2023/day/13

from utils import get_input

# Part 1

def find_mirror(pattern):

    def check_horiz(top, pattern):
        bot = top + 1
        while top >= 0 and bot < len(pattern):
            if pattern[top] != pattern[bot]:
                return False
            top -= 1
            bot += 1
        return True

    # check horizontal
    for i in range(len(pattern) - 1):
        if check_horiz(i, pattern):
            return 100 * (i + 1)
            
    # rotate the pattern (pythonic trick!!!)
    # r_pattern = [''.join(row[i] for row in pattern) for i in range(len(pattern[0]))]
    r_pattern = list(zip(*pattern))

    # check again (vertical this time)
    for i in range(len(r_pattern) - 1):
        if check_horiz(i, r_pattern):
            return i + 1
        
    return -1
            

# Part 2

def find_mirror_s(pattern):

    def check_horiz_s(top, pattern):
        bot = top + 1
        smudges = 0
        while top >= 0 and bot < len(pattern):
            if pattern[top] != pattern[bot]:
                # return False
                if smudges > 0:
                    return False
                else:
                    for (x, y) in zip(pattern[top], pattern[bot]):
                        if x != y:
                            smudges += 1
                        if smudges > 1:
                            return False
            top -= 1
            bot += 1
        return True if smudges == 1 else False

    # check horizontal
    for i in range(len(pattern) - 1):
        if check_horiz_s(i, pattern):
            return 100 * (i + 1)
            
    # rotate the pattern (pythonic trick!!!)
    # r_pattern = [''.join(row[i] for row in pattern) for i in range(len(pattern[0]))]
    r_pattern = list(zip(*pattern))

    # check again (vertical this time)
    for i in range(len(r_pattern) - 1):
        if check_horiz_s(i, r_pattern):
            return i + 1
        
    return -1
            

# -------- MAIN FUNCTION -------- #
def main():
    lines = get_input()
    patterns = []
    current_pattern = []

    for line in lines:
        if line:
            current_pattern.append(line)
        else:
            if current_pattern:
                patterns.append(current_pattern)
                current_pattern = []

    # add the last pattern
    if current_pattern:
        patterns.append(current_pattern)

    total = sum(find_mirror(p) or 0 for p in patterns)
    print(f"Part 1: {total}")

    total = sum(find_mirror_s(p) or 0 for p in patterns)
    print(f"Part 2: {total}")
        
    pass

if __name__ == "__main__":
    main()

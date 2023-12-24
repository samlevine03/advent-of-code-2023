# https://adventofcode.com/2023/day/14

from utils import get_input, input_to_2d_array

# Part 1

def get_load(lines):
    lines = list(map("".join, zip(*lines)))
    lines = ["#".join(["".join(sorted(list(group), reverse=True)) for group in row.split("#")]) for row in lines]
    lines = list(map("".join, zip(*lines)))

    return sum(row.count("O") * (len(lines) - r) for r, row in enumerate(lines))

# Part 2

def cycle(grid):
    for i in range(4):
        grid = tuple(map("".join, zip(*grid)))
        grid = tuple("#".join(["".join(sorted(tuple(group), reverse=True)) for group in row.split("#")]) for row in grid)
        grid = tuple(row[::-1] for row in grid)

    return grid
        


# -------- MAIN FUNCTION -------- #
def main():
    lines = get_input()
    arr = input_to_2d_array(lines)

    total = get_load(arr)
    print(f"Part 1: {total}")

    grid = tuple(lines)
    
    grids = {grid}
    arrs = [grid]
    idx = 0

    for _ in range(1000000000):
        idx += 1
        grid = cycle(grid)
        if grid in grids:
            first = arrs.index(grid)
            grid = arrs[(1000000000 - first) % (idx - first) + first]
            total = sum(row.count("O") * (len(grid) - r) for r, row in enumerate(grid))
            break
        grids.add(grid)
        arrs.append(grid)
    
    print(f"Part 2: {total}")


if __name__ == "__main__":
    main()

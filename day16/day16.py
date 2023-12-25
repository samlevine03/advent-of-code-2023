# https://adventofcode.com/2023/day/16

from collections import deque  # need this cuz we hit the recursion limit
from utils import get_input, input_to_2d_array

# Part 1

def shoot_beam(grid, start_r, start_c, start_dr, start_dc):
    beamed = set()
    q = deque([(start_r, start_c, start_dr, start_dc)])  # initial state with input starting point and direction

    while q:
        r, c, dr, dc = q.popleft()

        if (r, c, dr, dc) in beamed:
            continue
        beamed.add((r, c, dr, dc))

        r += dr
        c += dc

        if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]):
            continue

        ch = grid[r][c]

        if ch == "." or (ch == "-" and dc != 0) or (ch == "|" and dr != 0):
            q.append((r, c, dr, dc))
        elif ch == "/":
            q.append((r, c, -dc, -dr))
        elif ch == "\\":
            q.append((r, c, dc, dr))
        else:
            if ch == "|":
                possible_dirs = [(1, 0), (-1, 0)]
            elif ch == "-":
                possible_dirs = [(0, 1), (0, -1)]
            for new_dr, new_dc in possible_dirs:
                q.append((r, c, new_dr, new_dc))

    return beamed

# Part 2



# -------- MAIN FUNCTION -------- #
def main():
    lines = get_input()
    arr = input_to_2d_array(lines)
    beamed = shoot_beam(arr, 0, -1, 0, 1)
    coords = {(r, c) for (r, c, _, _) in beamed}

    part1 = len(coords) - 1
    print(f"Part 1: {part1}")

    max_beam = 0
    height, width = len(arr), len(arr[0])
    edge_positions = [(r, c) for r in range(height) for c in range(width) 
                    if r in {0, height - 1} or c in {0, width - 1}]

    for r, c in edge_positions:
        if (r, c) in coords:
            continue
        directions = [(0, 1), (1, 0)] if r in {0, height - 1} and c in {0, width - 1} else [(0, 1)]
        for dr, dc in directions:
            beamed = shoot_beam(arr, r, c, dr, dc)
            coords = {(r, c) for (r, c, _, _) in beamed}
            max_beam = max(max_beam, len(coords))

    print(f"Part 2: {max_beam}")


    pass

if __name__ == "__main__":
    main()

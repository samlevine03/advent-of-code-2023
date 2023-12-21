# https://adventofcode.com/2023/day/09

from utils import get_input, input_to_2d_array

# Part 1

def traverse(arr):

    dirs = ((0, -1), (0, 1), (-1, 0), (1, 0))

    def find_start(arr):
        return next((i, j) for i, row in enumerate(arr) for j, val in enumerate(row) if val == 'S')

    def get_starting_dir(arr, i, j):
        for dx, dy in dirs:
            if 0 <= i + dx < len(arr) and 0 <= j + dy < len(arr[i]):
                pipe = arr[i + dx][j + dy]
                if (dx, dy) == (0, -1) and pipe in 'L-F':
                    return dx, dy
                if (dx, dy) == (0, 1) and pipe in 'J-7':
                    return dx, dy
                if (dx, dy) == (-1, 0) and pipe in '7|F':
                    return dx, dy
                if (dx, dy) == (1, 0) and pipe in 'J|L':
                    return dx, dy
        return None


    start = find_start(arr)
    i, j = start

    prev_dir = None
    next_dir = get_starting_dir(arr, i, j)

    loop = ['S']
    loop_indices = set()
    loop_indices.add((i, j))
    i += next_dir[0]
    j += next_dir[1]

    while arr[i][j] != 'S':
        pipe = arr[i][j]
        loop.append(pipe)
        loop_indices.add((i, j))
        prev_dir = next_dir
        if pipe == '|' or pipe == '-':
            next_dir = prev_dir
        elif pipe == 'L':
            if prev_dir == (0, -1):
                next_dir = (-1, 0)
            elif prev_dir == (1, 0):
                next_dir = (0, 1)
        elif pipe == 'J':
            if prev_dir == (0, 1):
                next_dir = (-1, 0)
            elif prev_dir == (1, 0):
                next_dir = (0, -1)
        elif pipe == '7':
            if prev_dir == (0, 1):
                next_dir = (1, 0)
            elif prev_dir == (-1, 0):
                next_dir = (0, -1)
        elif pipe == 'F':
            if prev_dir == (0, -1):
                next_dir = (1, 0)
            elif prev_dir == (-1, 0):
                next_dir = (0, 1)
        i += next_dir[0]
        j += next_dir[1]

    return len(loop) // 2, loop_indices

# Part 2

def count_enclosed_tiles(arr, loop_indices):
    def enclosed(i, j):
        return sum(arr[i][k] in "F7|" for k in range(j) if (i, k) in loop_indices) % 2 != 0
    
    return sum(enclosed(i, j) for i in range(len(arr)) for j in range(len(arr[i])) if (i, j) not in loop_indices)




# -------- MAIN FUNCTION -------- #
def main():
    lines = get_input()
    arr = input_to_2d_array(lines)
    part1, loop_indices = traverse(arr)
    print(f'Part 1: {part1}')

    part2 = count_enclosed_tiles(arr, loop_indices)
    print(f'Part 2: {part2}')


if __name__ == "__main__":
    main()

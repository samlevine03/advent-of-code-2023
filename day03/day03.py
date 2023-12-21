# https://adventofcode.com/2023/day/03

from utils import get_input, input_to_2d_array

# Part 1

def scan_number(arr, i, j, scanned):
    if not arr[i][j].isdigit() or (i, j) in scanned:
        return 0

    num = arr[i][j]
    scanned.add((i, j))
    
    for k in range(j - 1, -1, -1):
        if arr[i][k].isdigit():
            num = arr[i][k] + num
            scanned.add((i, k))
        else:
            break
    
    for k in range(j + 1, len(arr[i])):
        if arr[i][k].isdigit():
            num += arr[i][k]
            scanned.add((i, k))
        else:
            break

    return int(num)


def sum_numbers_around(arr, i, j, scanned):
    dirs = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
    return sum(scan_number(arr, i + di, j + dj, scanned) 
               for di, dj in dirs 
               if 0 <= i + di < len(arr) and 0 <= j + dj < len(arr[0]))


def sum_part_numbers(arr):
    scanned = set()
    return sum(sum_numbers_around(arr, i, j, scanned) 
               for i in range(len(arr)) 
               for j in range(len(arr[i])) 
               if arr[i][j] != '.' and not arr[i][j].isdigit())

# Part 2

def calculate_gear_ratio(grid, row, col, scanned):
    if grid[row][col] != '*' or (row, col) in scanned:
        return 0

    directions = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
    part_numbers = []
    for dr, dc in directions:
        new_row, new_col = row + dr, col + dc
        if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]) and grid[new_row][new_col].isdigit() and (new_row, new_col) not in scanned:
            num = scan_number(grid, new_row, new_col, scanned)
            if num and num not in part_numbers:
                part_numbers.append(num)
                if len(part_numbers) > 2:
                    return 0  # Not a gear if more than 2 numbers

    scanned.add((row, col))
    return part_numbers[0] * part_numbers[1] if len(part_numbers) == 2 else 0


def sum_gear_ratios(arr):
    scanned = set()
    return sum(calculate_gear_ratio(arr, i, j, scanned) 
               for i in range(len(arr)) 
               for j in range(len(arr[i])) 
               if arr[i][j] == '*')

# -------- MAIN FUNCTION -------- #
def main():
    arr = input_to_2d_array(get_input())
    part1 = sum_part_numbers(arr)
    part2 = sum_gear_ratios(arr)

    print(f'Part 1: {part1}')
    print(f'Part 2: {part2}')

    return

if __name__ == "__main__":
    main()

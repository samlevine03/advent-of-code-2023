"""
--- Day 3: Gear Ratios ---

You and the Elf eventually reach a gondola lift station; he says the gondola
lift will take you up to the water source, but this is as far as he can bring
you. You go inside.

It doesn't take long to find the gondolas, but there seems to be a problem:
they're not moving.

"Aaah!"

You turn around to see a slightly-greasy Elf with a wrench and a look of
surprise. "Sorry, I wasn't expecting anyone! The gondola lift isn't working
right now; it'll still be a while before I can fix it." You offer to help.

The engineer explains that an engine part seems to be missing from the engine,
but nobody can figure out which one. If you can add up all the part numbers in
the engine schematic, it should be easy to work out which part is missing.

The engine schematic (your puzzle input) consists of a visual representation of
the engine. There are lots of numbers and symbols you don't really understand,
but apparently any number adjacent to a symbol, even diagonally, is a 
"partnumber" and should be included in your sum. (Periods (.) do not count 
as a symbol.)

Here is an example engine schematic:

467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..

In this schematic, two numbers are not part numbers because they are not
adjacent to a symbol: 114 (top right) and 58 (middle right). Every other number
is adjacent to a symbol and so is a part number; their sum is 4361.

Of course, the actual engine schematic is much larger. What is the sum of all
of the part numbers in the engine schematic?
"""

from utils import get_input, input_to_2d_array


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

"""
--- Part Two ---

The engineer finds the missing part and installs it in the engine! As the
engine springs to life, you jump in the closest gondola, finally ready to
ascend to the water source.

You don't seem to be going very fast, though. Maybe something is still
wrong? Fortunately, the gondola has a phone labeled "help", so you pick it up
and the engineer answers.

Before you can explain the situation, she suggests that you look out the
window. There stands the engineer, holding a phone in one hand and waving with
the other. You're going so slowly that you haven't even left the station. 
You exit the gondola.

The missing part wasn't the only issue - one of the gears in the engine is
wrong. A gear is any * symbol that is adjacent to exactly two part numbers.
Its gear ratio is the result of multiplying those two numbers together.

This time, you need to find the gear ratio of every gear and add them all up
so that the engineer can figure out which gear needs to be replaced.

Consider the same engine schematic again:

467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..

In this schematic, there are two gears. The first is in the top left; it has
part numbers 467 and 35, so its gear ratio is 16345. The second gear is in the
lower right; its gear ratio is 451490. (The * adjacent to 617 is not a gear
because it is only adjacent to one part number.) Adding up all of the gear 
ratios produces 467835.

What is the sum of all of the gear ratios in your engine schematic?
"""

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

def main():
    arr = input_to_2d_array(get_input())
    part1 = sum_part_numbers(arr)
    part2 = sum_gear_ratios(arr)

    print(f'Part 1: {part1}')
    print(f'Part 2: {part2}')

    return

if __name__ == '__main__':
    main()
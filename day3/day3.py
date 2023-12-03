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
    # Check if the current element is not a number or already scanned
    if not arr[i][j].isdigit() or (i, j) in scanned:
        return 0

    # Scan for a complete number
    num = arr[i][j]
    # Look left
    k = j - 1
    while k >= 0 and arr[i][k].isdigit():
        num = arr[i][k] + num
        scanned.add((i, k))  # Mark as scanned
        k -= 1
    # Look right
    k = j + 1
    while k < len(arr[i]) and arr[i][k].isdigit():
        num += arr[i][k]
        scanned.add((i, k))  # Mark as scanned
        k += 1

    scanned.add((i, j))  # Mark the original digit as scanned
    return int(num)


def sum_numbers_around(arr, i, j, scanned):
    # Include diagonal directions
    dirs = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
    sum = 0
    for dir in dirs:
        ni, nj = i + dir[0], j + dir[1]
        # Check bounds
        if 0 <= ni < len(arr) and 0 <= nj < len(arr[0]):
            sum += scan_number(arr, ni, nj, scanned)
    return sum


def sum_part_numbers(arr):
    scanned = set()
    total_sum = 0
    # Look through the array for a symbol that isn't a '.'
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] != '.' and (i, j) not in scanned and not arr[i][j].isdigit():
                # Add up all the numbers around it
                total_sum += sum_numbers_around(arr, i, j, scanned)
    return total_sum

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

def calculate_gear_ratio(arr, i, j, scanned):
    if arr[i][j] != '*' or (i, j) in scanned:
        return 0

    part_numbers = []
    dirs = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
    for dir in dirs:
        ni, nj = i + dir[0], j + dir[1]
        if 0 <= ni < len(arr) and 0 <= nj < len(arr[0]):
            # Scan for a complete number
            if arr[ni][nj].isdigit() and (ni, nj) not in scanned:
                num = scan_number(arr, ni, nj, scanned)
                if num and num not in part_numbers:
                    part_numbers.append(num)
                if len(part_numbers) > 2:
                    return 0  # Not a gear if more than 2 numbers

    scanned.add((i, j))  # Mark the gear as processed
    if len(part_numbers) == 2:
        # Multiply the two part numbers to get the gear ratio
        return part_numbers[0] * part_numbers[1]
    else:
        return 0


def sum_gear_ratios(arr):
    scanned = set()
    gear_ratio_sum = 0
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == '*':
                gear_ratio_sum += calculate_gear_ratio(arr, i, j, scanned)
    return gear_ratio_sum


def main():
    arr = input_to_2d_array(get_input())
    print(sum_part_numbers(arr))
    print(sum_gear_ratios(arr))
    

    return

if __name__ == '__main__':
    main()
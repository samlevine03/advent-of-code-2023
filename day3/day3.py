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


def main():
    arr = input_to_2d_array(get_input())
    print(sum_part_numbers(arr))
    

    return

if __name__ == '__main__':
    main()
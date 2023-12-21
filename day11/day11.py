from utils import get_input, input_to_2d_array

# https://adventofcode.com/2023/day/11
# Part 1

def get_galaxy_coords(arr):
    coordinates = [(i, j) for i, row in enumerate(arr) for j, val in enumerate(row) if val == '#']
    return coordinates

def get_empty_rows_and_cols(arr):
    empty_rows = [all(val == '.' for val in row) for row in arr]
    empty_cols = [all(row[i] == '.' for row in arr) for i in range(len(arr[0]))]
    return empty_rows, empty_cols

def dist(g1, g2, empty_rows, empty_cols, empty_size):
    i_g1, j_g1 = g1
    i_g2, j_g2 = g2
    dist = abs(i_g1 - i_g2) + abs(j_g1 - j_g2)
    dist += sum([empty_size for i in range(min(i_g1, i_g2), max(i_g1, i_g2)) if empty_rows[i]])
    dist += sum([empty_size for j in range(min(j_g1, j_g2), max(j_g1, j_g2)) if empty_cols[j]])
    return dist

# Part 2

# just added the empty_size parameter to the dist function :)

# -------- MAIN FUNCTION -------- #
def main():
    lines = get_input()
    arr = input_to_2d_array(lines)
    coords = (get_galaxy_coords(arr))
    empty_rows, empty_cols = get_empty_rows_and_cols(arr)
    total = sum([dist(coords[i], coords[j], empty_rows, empty_cols, 1) for i in range(len(coords)) for j in range(i + 1, len(coords))])
    
    print(f"Part 1: {total}")

    total = sum([dist(coords[i], coords[j], empty_rows, empty_cols, (1000000-1)) for i in range(len(coords)) for j in range(i + 1, len(coords))])
    print(f"Part 2: {total}")
    pass

if __name__ == "__main__":
    main()

# https://adventofcode.com/2023/day/15

from utils import get_input

# Part 1

def hash(string):
    # determine the ascii code for the current char of the string
    # increase the current value by the ascii code
    # set the current value to itself multiplied by 17
    # set the current value to the remainder of dividing itself by 256
    res = 0
    for c in string:
        res += ord(c)
        res *= 17
        res = res % 256
    return res

# Part 2



# -------- MAIN FUNCTION -------- #
def main():
    lines = get_input()
    inputs = lines[0].split(",")
    total = sum(map(hash, inputs))
    print(f"Part 1: {total}")

    boxes = [[] for _ in range(256)]
    lengths = {}
    for input in inputs:
        if '=' in input:
            label, length = input.split('=')
            idx = hash(label)
            if label not in boxes[idx]:
                boxes[idx].append(label)
            lengths[label] = int(length)
        else:
            label, _ = input.split('-')
            idx = hash(label)
            if label in boxes[idx]:
                boxes[idx].remove(label)

    total = sum(box_idx * lens_idx * lengths[lens] for box_idx, box in enumerate(boxes, 1) for lens_idx, lens in enumerate(box, 1))

    print(f"Part 2: {total}")



    pass

if __name__ == "__main__":
    main()

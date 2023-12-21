# https://adventofcode.com/2023/day/05

from utils import get_input

# Part 1

def parse_input(lines):
    seeds = []
    maps = {}
    i = 0

    while i < len(lines):
        line = lines[i]
        if line.startswith("seeds:"):
            seeds = [int(s) for s in line.split()[1:]]
        elif line.endswith("map:"):
            cur_map = line.split()[0]
            maps[cur_map] = []
        else:
            if line == "":
                i += 1
                continue
            maps[cur_map].append([int(s) for s in line.split()])
        i += 1

    return seeds, maps

def convert_through_maps(seeds, maps):
    def convert_number(number, conversion_map):
        # Check each mapping range in the conversion map
        for dest_start, src_start, length in conversion_map:
            if src_start <= number < src_start + length:
                # Calculate the offset from the start of the source range
                offset = number - src_start
                # Apply the same offset to the destination range
                return dest_start + offset
        # If the number is not in any range, it maps to itself
        return number

    location_numbers = []
    for seed in seeds:
        current_number = seed
        for key in maps.keys():
            current_number = convert_number(current_number, maps[key])
        location_numbers.append(current_number)

    return min(location_numbers)

# Part 2

def get_seed_ranges(seeds):
    seed_ranges = []
    for i in range(0, len(seeds), 2):
        seed_ranges.append([seeds[i], seeds[i] + seeds[i+1]])
    return seed_ranges


def translate_seed_ranges(seed_ranges, maps):
    # Seed ranges are a list of [start, end] pairs
    # Maps are a dict of lists of [dest_start, src_start, length] triples
    for map in maps.values():
        new = []
        while seed_ranges:
            start, end = seed_ranges.pop()
            for dest_start, src_start, length in map:
                overlap_l = max(start, src_start)
                overlap_r = min(end, src_start + length)
                if overlap_l < overlap_r:
                    new.append((overlap_l - src_start + dest_start, overlap_r - src_start + dest_start))
                    if overlap_l > start:
                        seed_ranges.append((start, overlap_l))
                    if end > overlap_r:
                        seed_ranges.append((overlap_r, overlap_r))
                    break
            else:
                new.append((start, end))
        seed_ranges = new
    return seed_ranges

# -------- MAIN FUNCTION -------- #
def main():
    lines = get_input()
    seeds, maps = parse_input(lines)
    result = convert_through_maps(seeds, maps)
    print(f"Part 1 Result: {result}")


    seed_ranges = get_seed_ranges(seeds)
    translated = translate_seed_ranges(seed_ranges, maps)
    result = min(translated)[0]
    print(f"Part 2 Result: {result}")

if __name__ == "__main__":
    main()

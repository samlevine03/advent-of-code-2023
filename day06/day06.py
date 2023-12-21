# https://adventofcode.com/2023/day/06

from utils import get_input

# Part 1

def get_race_records(lines):
    lengths = list(map(int, lines[0].split()[1:]))
    records = list(map(int, lines[1].split()[1:]))
    return list(zip(lengths, records))


def mult_num_ways_to_win(races):
    result = 1
    for time, dist in races:
        num_ways = sum(travel > dist for charge_time in range(time) for travel in [charge_time * (time - charge_time)])
        result *= num_ways
    return result

# Part 2

def get_new_race_records(lines):
    length, record = int(lines[0].split(':')[1].replace(' ','')), int(lines[1].split(':')[1].replace(' ',''))
    return (length, record)

def num_ways_to_win(race):
    time, dist = race
    return sum(charge_time * (time - charge_time) > dist for charge_time in range(time))

# -------- MAIN FUNCTION -------- #
def main():
    lines = get_input()
    races = get_race_records(lines)
    result = mult_num_ways_to_win(races)
    print(f"Part 1 Result: {result}")

    race = get_new_race_records(lines)
    result = num_ways_to_win(race)
    print(f"Part 2 Result: {result}")

if __name__ == "__main__":
    main()

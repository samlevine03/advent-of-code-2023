# https://adventofcode.com/2023/day/06

from utils import get_input

# Part 1

def get_race_records(lines):
    length, record = list(map(int, lines[0].split()[1:])), list(map(int, lines[1].split()[1:]))
    races = []
    for i in range(len(length)):
        races.append((length[i], record[i]))
    return races


def mult_num_ways_to_win(races):
    mult = 1
    for time, dist in races:
        num_ways = 0
        for charge_time in range(time):
            travel_time = time - charge_time
            travel = charge_time * travel_time
            if travel > dist:
                num_ways += 1
        mult *= num_ways
    return mult

# Part 2

def get_new_race_records(lines):
    length, record = int(lines[0].split(':')[1].replace(' ','')), int(lines[1].split(':')[1].replace(' ',''))
    return (length, record)

def num_ways_to_win(race):
    time, dist = race
    num_ways = 0
    for charge_time in range(time):
        travel_time = time - charge_time
        travel = charge_time * travel_time
        if travel > dist:
            num_ways += 1
    return num_ways

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

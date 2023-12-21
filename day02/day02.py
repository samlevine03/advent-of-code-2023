# https://adventofcode.com/2023/day/02

from utils import get_input

# Part 1

def parse_game_data(game):
    game_id, data = game.split(':')
    game_id = int(game_id.split()[1])
    data = data.replace(';', ',').split(',')
    largest_sets = {'red': 0, 'green': 0, 'blue': 0}

    for grab in data:
        num, color = grab.split()
        num = int(num)
        largest_sets[color] = max(largest_sets[color], num)

    return game_id, largest_sets

def check_game(game):
    game_id, largest_sets = parse_game_data(game)
    if all(largest_sets[color] <= limit for color, limit in [('red', 12), ('green', 13), ('blue', 14)]):
        return game_id
    return 0

# Part 2

def get_power_set(game):
    _, largest_sets = parse_game_data(game)
    return largest_sets['red'] * largest_sets['green'] * largest_sets['blue']

# -------- MAIN FUNCTION -------- #
def main():
    """
    Main program.
    """
    games = get_input()
    total_possible = sum(check_game(game) for game in games)
    total_power = sum(get_power_set(game) for game in games)
    print(f'Part 1: {total_possible}')
    print(f'Part 2: {total_power}')

if __name__ == "__main__":
    main()

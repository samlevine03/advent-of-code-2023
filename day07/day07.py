# https://adventofcode.com/2023/day/07

from utils import get_input

# Part 1

def get_type(hand):
    """
    Returns the rank of a hand
    """
    type = 0
    counts = {card: hand.count(card) for card in hand}
    if 5 in counts.values():
        type = 7
    elif 4 in counts.values():
        type = 6
    elif 3 in counts.values() and 2 in counts.values():
        type = 5
    elif 3 in counts.values():
        type = 4
    elif list(counts.values()).count(2) == 2:
        type = 3
    elif 2 in counts.values():
        type = 2
    else:
        type = 1
    return type


def hand_to_sort_value(hand):
    card_values = {"A": 14, "K": 13, "Q": 12, "J": 11, "T": 10, "9": 9, "8": 8, "7": 7, "6": 6, "5": 5, "4": 4, "3": 3, "2": 2}
    return tuple(card_values[card] for card in hand)

# Part 2

def get_type_joker(hand):
    old_type = get_type(hand)
    num_jokers = hand.count("J")
    hand_without_jokers = hand.replace("J", "")
    without_jokers_type = get_type(hand_without_jokers)

    # handle case with 4 or 5 jokers
    if num_jokers >= 4:
        return 7
    
    # handle case with 3 jokers
    if num_jokers == 3:
        # we can either get 4 or 5 of a kind
        return 6 if without_jokers_type == 1 else 7

    # handle case with 2 jokers
    if num_jokers == 2:
        # we can either get 3, 4, or 5 of a kind
        if without_jokers_type == 1:
            return 4
        elif without_jokers_type == 2:
            return 6
        return 7
    
    # handle case with 1 joker
    if num_jokers == 1:
        # we can get 2, 3, 4, or 5 of a kind
        if without_jokers_type == 1:
            return 2
        elif without_jokers_type == 2:
            return 4
        elif without_jokers_type == 3:
            return 5
        elif without_jokers_type == 4:
            return 6
        return 7
    
    # handle case with no jokers
    return old_type


def hand_to_sort_value_joker(hand):
    card_values = {"A": 14, "K": 13, "Q": 12, "J": 0, "T": 10, "9": 9, "8": 8, "7": 7, "6": 6, "5": 5, "4": 4, "3": 3, "2": 2}
    return tuple(card_values[card] for card in hand)

# -------- MAIN FUNCTION -------- #
def main():
    lines = get_input()
    hands = [(get_type(hand), hand, int(bid)) for line in lines for hand, bid in [line.split()]]
    sorted_hands = sorted(hands, key=lambda x: (x[0], hand_to_sort_value(x[1])), reverse=True)
    total_score = sum((len(hands) - rank + 1) * bid for rank, (_, _, bid) in enumerate(sorted_hands, start=1))
    print(f"Part 1 Score: {total_score}")

    hands = [(get_type_joker(hand), hand, int(bid)) for line in lines for hand, bid in [line.split()]]
    sorted_hands = sorted(hands, key=lambda x: (x[0], hand_to_sort_value_joker(x[1])), reverse=True)
    total_score = sum((len(hands) - rank + 1) * bid for rank, (_, _, bid) in enumerate(sorted_hands, start=1))
    print(f"Part 2 Score: {total_score}")

if __name__ == "__main__":
    main()

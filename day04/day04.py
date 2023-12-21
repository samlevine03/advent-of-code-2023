# https://adventofcode.com/2023/day/04

from utils import get_input

# Part 1

def parse_card(card):
    card_num, card_contents = card.split(":")
    card_idx = int(card_num.split()[1]) - 1
    winning_numbers, your_numbers = card_contents.split("|")
    winning_numbers = set(map(int, winning_numbers.split()))
    your_numbers = set(map(int, your_numbers.split()))
    return [card_idx, winning_numbers, your_numbers, 1]


def score_card(winning_numbers, your_numbers):
    score = 0
    for num in your_numbers:
        if num in winning_numbers:
            score = 1 if score == 0 else score * 2
    return score

# Part 2

def card_matches(your_numbers, winning_numbers):
    return len(your_numbers.intersection(winning_numbers))

# -------- MAIN FUNCTION -------- #
def main():
    total_score = 0
    cards = list(map(parse_card, get_input()))
    total_score = sum([score_card(card[1], card[2]) for card in cards])
    print(f"Total score (Part 1): {total_score}")

    num_cards = 0
    cards = list(map(parse_card, get_input()))
    for idx, nums, winning_nums, num_copies in cards:
        matches = card_matches(nums, winning_nums)
        num_cards += num_copies
        for i in range(matches):
            next_idx = idx + i + 1
            if next_idx < len(cards):
                cards[next_idx][3] += num_copies

    print(f"Number of cards (Part 2): {num_cards}")

if __name__ == "__main__":
    main()

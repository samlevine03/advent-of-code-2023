from utils import get_input

"""
--- Day 7: Camel Cards ---

Your all-expenses-paid trip turns out to be a one-way, five-minute ride in an airship . (At least it's a *cool* airship !) It drops you off at the edge of a vast desert and descends back to Island Island.

"Did you bring the parts?"

You turn around to see an Elf completely covered in white clothing, wearing goggles, and riding a large camel .

"Did you bring the parts?" she asks again, louder this time. You aren't sure what parts she's looking for; you're here to figure out why the sand stopped.

"The parts! For the sand, yes! Come with me; I will show you." She beckons you onto the camel.

After riding a bit across the sands of Desert Island, you can see what look like very large rocks covering half of the horizon. The Elf explains that the rocks are all along the part of Desert Island that is directly above Island Island, making it hard to even get there. Normally, they use big machines to move the rocks and filter the sand, but the machines have broken down because Desert Island recently stopped receiving the *parts* they need to fix the machines.

You've already assumed it'll be your job to figure out why the parts stopped when she asks if you can help. You agree automatically.

Because the journey will take a few days, she offers to teach you the game of *Camel Cards* . Camel Cards is sort of similar to poker except it's designed to be easier to play while riding a camel.

In Camel Cards, you get a list of *hands* , and your goal is to order them based on the *strength* of each hand. A hand consists of *five cards* labeled one of `A` , `K` , `Q` , `J` , `T` , `9` , `8` , `7` , `6` , `5` , `4` , `3` , or `2` . The relative strength of each card follows this order, where `A` is the highest and `2` is the lowest.

Every hand is exactly one *type* . From strongest to weakest, they are:

 - *Five of a kind* , where all five cards have the same label: `AAAAA`
 - *Four of a kind* , where four cards have the same label and one card has a different label: `AA8AA`
 - *Full house* , where three cards have the same label, and the remaining two cards share a different label: `23332`
 - *Three of a kind* , where three cards have the same label, and the remaining two cards are each different from any other card in the hand: `TTT98`
 - *Two pair* , where two cards share one label, two other cards share a second label, and the remaining card has a third label: `23432`
 - *One pair* , where two cards share one label, and the other three cards have a different label from the pair and each other: `A23A4`
 - *High card* , where all cards' labels are distinct: `23456`

Hands are primarily ordered based on type; for example, every *full house* is stronger than any *three of a kind* .

If two hands have the same type, a second ordering rule takes effect. Start by comparing the *first card in each hand* . If these cards are different, the hand with the stronger first card is considered stronger. If the first card in each hand have the *same label* , however, then move on to considering the *second card in each hand* . If they differ, the hand with the higher second card wins; otherwise, continue with the third card in each hand, then the fourth, then the fifth.

So, `33332` and `2AAAA` are both *four of a kind* hands, but `33332` is stronger because its first card is stronger. Similarly, `77888` and `77788` are both a *full house* , but `77888` is stronger because its third card is stronger (and both hands have the same first and second card).

To play Camel Cards, you are given a list of hands and their corresponding *bid* (your puzzle input). For example:

```
32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
```

This example shows five hands; each hand is followed by its *bid* amount. Each hand wins an amount equal to its bid multiplied by its *rank* , where the weakest hand gets rank 1, the second-weakest hand gets rank 2, and so on up to the strongest hand. Because there are five hands in this example, the strongest hand will have rank 5 and its bid will be multiplied by 5.

So, the first step is to put the hands in order of strength:

 - `32T3K` is the only *one pair* and the other hands are all a stronger type, so it gets rank *1* .
 - `KK677` and `KTJJT` are both *two pair* . Their first cards both have the same label, but the second card of `KK677` is stronger ( `K` vs `T` ), so `KTJJT` gets rank *2* and `KK677` gets rank *3* .
 - `T55J5` and `QQQJA` are both *three of a kind* . `QQQJA` has a stronger first card, so it gets rank *5* and `T55J5` gets rank *4* .

Now, you can determine the total winnings of this set of hands by adding up the result of multiplying each hand's bid with its rank ( `765` * 1 + `220` * 2 + `28` * 3 + `684` * 4 + `483` * 5). So the *total winnings* in this example are `*6440*` .

Find the rank of every hand in your set. *What are the total winnings?*
"""

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
    """
    Convert a hand to a tuple representing its sort order.
    """
    card_values = {"A": 14, "K": 13, "Q": 12, "J": 11, "T": 10, "9": 9, "8": 8, "7": 7, "6": 6, "5": 5, "4": 4, "3": 3, "2": 2}
    return tuple(card_values[card] for card in hand)


"""
--- Part Two ---

To make things a little more interesting, the Elf introduces one additional rule. Now, J cards are jokers - wildcards that can act like whatever card would make the hand the strongest type possible.

To balance this, J cards are now the weakest individual cards, weaker even than 2. The other cards stay in the same order: A, K, Q, T, 9, 8, 7, 6, 5, 4, 3, 2, J.

J cards can pretend to be whatever card is best for the purpose of determining hand type; for example, QJJQ2 is now considered four of a kind. However, for the purpose of breaking ties between two hands of the same type, J is always treated as J, not the card it's pretending to be: JKKK2 is weaker than QQQQ2 because J is weaker than Q.

Now, the above example goes very differently:

32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483

    32T3K is still the only one pair; it doesn't contain any jokers, so its strength doesn't increase.
    KK677 is now the only two pair, making it the second-weakest hand.
    T55J5, KTJJT, and QQQJA are now all four of a kind! T55J5 gets rank 3, QQQJA gets rank 4, and KTJJT gets rank 5.

With the new joker rule, the total winnings in this example are 5905.

Using the new joker rule, find the rank of every hand in your set. What are the new total winnings?

"""

def get_type_joker(hand):
    """
    Returns the rank of a hand with jokers
    """
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
    """
    Convert a hand to a tuple representing its sort order with jokers.
    """
    card_values = {"A": 14, "K": 13, "Q": 12, "J": 0, "T": 10, "9": 9, "8": 8, "7": 7, "6": 6, "5": 5, "4": 4, "3": 3, "2": 2}
    return tuple(card_values[card] for card in hand)


# -------- MAIN FUNCTION -------- #
def main():
    lines = get_input()

    # hands_by_type = {
    #     1: [],  # High card
    #     2: [],  # One pair
    #     3: [],  # Two pair
    #     4: [],  # Three of a kind
    #     5: [],  # Full house
    #     6: [],  # Four of a kind
    #     7: []   # Five of a kind
    # }
    # for line in lines:
    #     hand, bid = line.split()
    #     hand_type = get_type(hand)
    #     hands_by_type[hand_type].append((hand, bid))

    hands = [(get_type(hand), hand, int(bid)) for line in lines for hand, bid in [line.split()]]

    # for type in hands_by_type:
    #     hands_by_type[type].sort(key=lambda x: hand_to_sort_value(x[0]))

    sorted_hands = sorted(hands, key=lambda x: (x[0], hand_to_sort_value(x[1])), reverse=True)

    total_score = 0
    # rank = 1
    # for type in hands_by_type:
    #     for hand, bid in hands_by_type[type]:
    #         total_score += rank * int(bid)
    #         rank += 1

    total_score = sum((len(hands) - rank + 1) * bid for rank, (_, _, bid) in enumerate(sorted_hands, start=1))

    print(f"Part 1 Score: {total_score}")

    # Part 2
    hands = [(get_type_joker(hand), hand, int(bid)) for line in lines for hand, bid in [line.split()]]
    sorted_hands = sorted(hands, key=lambda x: (x[0], hand_to_sort_value_joker(x[1])), reverse=True)
    total_score = sum((len(hands) - rank + 1) * bid for rank, (_, _, bid) in enumerate(sorted_hands, start=1))
    print(f"Part 2 Score: {total_score}")

if __name__ == "__main__":
    main()

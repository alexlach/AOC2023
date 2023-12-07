from collections import Counter

def score_hand(hand):
    hand_counts = list(Counter(hand).values())
    if 5 in hand_counts:
        return "0"  # five of a kind
    if 4 in hand_counts:
        return "1"  # four of a kind
    if 3 in hand_counts:
        if 2 in hand_counts:
            return "2"  # full house
        return "3"  # three of a kind
    if hand_counts.count(2) == 2:
        return "4"  # two pair
    if 2 in hand_counts:
        return "5"  # two of a kind
    return "6"  # high card

# Part 1
rows = open("07/test.txt").read().split("\n")
results = []
for row in rows:
    hand, bid = row.split(" ")
    trans_table = str.maketrans('AKQJT98765432', 'abcdefghijklm')
    hand_encoded = score_hand(hand) + hand.translate(trans_table)
    results.append((hand_encoded, bid))

results.sort(key=lambda x: x[0], reverse=True)  # sort encoded hands alphabetically
score = sum([int(x[1]) * (ind + 1) for ind, x in enumerate(results)])
print(score)

# Part 2
results = []
for row in rows:
    hand, bid = row.split(" ")
    # Generate all possible hands by replacing 'J's
    possible_hands = [hand]
    j_indices = [i for i, card in enumerate(hand) if card == "J"]
    for j_index in j_indices:
        new_possible_hands = []
        for possible_hand in possible_hands:
            for replacement_card in "AKQT98765432":
                new_possible_hands.append(possible_hand[:j_index] + replacement_card + possible_hand[j_index + 1:])
        possible_hands = new_possible_hands

    trans_table = str.maketrans('AKQJT98765432', 'abczefghijklm')
    hand_encoded = min(score_hand(h) for h in possible_hands) + hand.translate(trans_table)
    results.append((hand_encoded, bid))

results.sort(key=lambda x: x[0], reverse=True)
score = sum([int(bid) * (ind + 1) for ind, (_, bid) in enumerate(results)])
print(score)

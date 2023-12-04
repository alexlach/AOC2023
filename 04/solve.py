cards = open("04/input.txt").read().split("\n")

# part 1
scores = []
for card in cards:
    winning, mine = card[8:].replace("  ", " ").split(" | ")
    winning = winning.split(" ")
    mine = mine.split(" ")
    matches = set(winning) & set(mine)
    scores.append(int(2 ** (len(matches) - 1)))
print(sum(scores))

# Part 2
count_dict = {k: 1 for k in range(len(cards))}
for idx, card in enumerate(cards):
    winning, mine = card[8:].replace("  ", " ").split(" | ")
    winning = winning.split(" ")
    mine = mine.split(" ")
    matches = set(winning) & set(mine)
    for i in range(len(matches)):
        count_dict[idx + i + 1] = count_dict.get(idx + i + 1, 0) + count_dict[idx]
print(sum(count_dict.values()))
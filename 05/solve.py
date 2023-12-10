mappys = open("05/input.txt").read().split("\n\n")

seeds = mappys.pop(0).split(" ")[1:]
seeds = [int(i) for i in seeds]

# part 1
for mappy in mappys:
    mapping_tuples = []
    groups = mappy.split("\n")[1:]
    for group_range in groups:
        group_range = group_range.split(" ")
        group_range = [int(i) for i in group_range]
        mapping_tuples.append((group_range[1], group_range[1] + group_range[2], group_range[0] - group_range[1]))
    for idx, seed in enumerate(seeds):
        for mapping_tuple in mapping_tuples:
            if mapping_tuple[0] <= seed < mapping_tuple[1]:
                seeds[idx] = seed + mapping_tuple[2]
                break
print(min(seeds))

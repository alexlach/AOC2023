directions, maps = open("08/input.txt").read().replace("(", "").replace(")", "").split("\n\n")
directions = directions.translate(str.maketrans('LR', '01'))

# build out our map
direct_dict = {}
for line in maps.split("\n"):
    key, value = line.split(" = ")
    direct_dict[key] = tuple(value.split(", "))

# part 1
location = "AAA"
steps = 0
while location != "ZZZ":
    location = direct_dict[location][int(directions[steps % len(directions)])]
    steps += 1
print(steps)

# Part 2
start_nodes = [k for k in direct_dict.keys() if k.endswith("A")]
steps_to_end = {}
for node in start_nodes:
    steps = 0
    while node[-1] != "Z":
        node = direct_dict[node][int(directions[steps % len(directions)])]
        steps += 1
    steps_to_end[node] = steps
import math
lcm_result = math.lcm(*list(steps_to_end.values()))
print(lcm_result)

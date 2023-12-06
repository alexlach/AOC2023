import re
text = re.sub(' +', ' ', open("06/input.txt").read())
text = text.replace("Time: ", "").replace("Distance: ", "")

# part 1
# there's will be a min hold_time and a max hold_time, with times in between being more efficient
# distance = time_hold * (total_time - time_hold)
# time_hold = total_time / 2 +- (-4 * distance + total_time ** 2) ** 0.5 / 2
times, distances = text.split("\n")
races = [(int(t), int(d)) for t, d in zip(times.split(" "), distances.split(" "))]
options = []
for race in races:
    time, dist = race
    time_hold_max = int(time / 2 + (-4 * dist + time ** 2) ** 0.5 / 2 - 0.0001)  # -0.0001 to account for breaking ties
    time_hold_min = int(time / 2 - (-4 * dist + time ** 2) ** 0.5 / 2 + 0.0001) + 1
    options.append(time_hold_max - time_hold_min + 1)
import math
print(math.prod(options))

# part 2
time, dist = text.replace(" ", "").split("\n")
time_hold_max = int(int(time) / 2 + (-4 * int(dist) + int(time) ** 2) ** 0.5 / 2 - 0.0001)
time_hold_min = int(int(time) / 2 - (-4 * int(dist) + int(time) ** 2) ** 0.5 / 2 + 0.0001) + 1
print(time_hold_max - time_hold_min + 1)
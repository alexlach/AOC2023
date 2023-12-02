rows = open("02/input.txt").read().split("\n")

# part 1
possible_cubes = {"red": 12, "green": 13, "blue": 14}
all_games = []
invalid_games = []
for game in rows:
    game_num, pulls = game.split(": ")
    game_id = int(game_num.split(" ")[1])
    all_games.append(game_id)
    cube_sets = pulls.replace(",", ";").split("; ")  # it doesn't matter when bricks were pulled
    for cube_set in cube_sets:
        count, color = cube_set.split(" ")
        if int(count) > possible_cubes.get(color, 0):
            invalid_games.append(game_id)
print(sum(set(all_games) - set(invalid_games)))

# part 2
powers = []
for game in rows:
    game_num, pulls = game.split(": ")
    cube_sets = pulls.replace(",", ";").split("; ")  # it doesn't matter when bricks were pulled
    max_cubes = {}
    for cube_set in cube_sets:
        count, color = cube_set.split(" ")
        max_cubes[color] = max(max_cubes.get(color, 0), int(count))
    powers.append(max_cubes.get("red", 0) * max_cubes.get("green", 0) * max_cubes.get("blue", 0))
print(sum(powers))

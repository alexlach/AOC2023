from collections import deque

rows = open("10/input.txt").read().split("\n")
grid = [list(row) for row in rows]

# add a border of ground around the grid
grid = [["."] * (len(grid[0]) + 2)] + [["."] + row + ["."] for row in grid] + [["."] * (len(grid[0]) + 2)]

# find location of the S
start = next((x, y) for y in range(len(grid)) for x in range(len(grid[y])) if grid[y][x] == "S")

def find_connections(loc):
    connecting_locs = []
    if grid[loc[1] - 1][loc[0]] in ("|", "7", "F", "S"):  # check north
        if grid[loc[1]][loc[0]] in ("|", "L", "J", "S"):
            connecting_locs.append((loc[0], loc[1] - 1))
    if grid[loc[1] + 1][loc[0]] in ("|", "L", "J", "S"):  # check south
        if grid[loc[1]][loc[0]] in ("|", "7", "F", "S"):
            connecting_locs.append((loc[0], loc[1] + 1))
    if grid[loc[1]][loc[0] - 1] in ("-", "F", "L", "S"):  # check west
        if grid[loc[1]][loc[0]] in ("-", "7", "J", "S"):
            connecting_locs.append((loc[0] - 1, loc[1]))
    if grid[loc[1]][loc[0] + 1] in ("-", "7", "J", "S"):  # check east
        if grid[loc[1]][loc[0]] in ("-", "F", "L", "S"):
            connecting_locs.append((loc[0] + 1, loc[1]))
    return connecting_locs

unmapped_locs = [start]
connect_map = {}
while unmapped_locs:
    loc = unmapped_locs.pop()
    if loc in connect_map:
        continue
    connect_map[loc] = find_connections(loc)
    unmapped_locs += connect_map[loc]

def bfs_shortest_path(connect_map, start):
    queue = deque([(start, 0)])  # Initialize with the start location
    distances = {start: 0}
    while queue:
        current_loc, current_dist = queue.popleft()
        for neighbor in connect_map[current_loc]:
            if neighbor not in distances:
                distances[neighbor] = current_dist + 1
                queue.append((neighbor, current_dist + 1))
    return distances

distances = bfs_shortest_path(connect_map, start)
print(max(distances.values()))

# clean up grid, converting all non-connecting locations to ground
for j in range(len(grid)):
    for i in range(len(grid[0])):
        if (i, j) not in connect_map.keys():
            grid[j][i] = '.'

enclosed = []
for i in range(len(grid)):
    currently_enclosed = False
    for j in range(len(grid[0])):
        if grid[i][j] in "|JLS":
            currently_enclosed = not currently_enclosed
        else:
            if currently_enclosed:
                if (j, i) not in connect_map.keys():
                    enclosed.append((i, j))

print(len(enclosed))
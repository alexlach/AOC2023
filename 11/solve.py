rows = open("11/input.txt").read().split("\n")

grid = [list(row) for row in rows]

row_indices_without_hash = []
for i in range(len(grid)):
    if not "#" in grid[i]:
        row_indices_without_hash.append(i)
print(f"row indices without hash: {row_indices_without_hash}")

col_indices_without_hash = []
for col_ind in range(len(grid[0])):
    col = [row[col_ind] for row in grid]
    if not "#" in col:
        col_indices_without_hash.append(col_ind)
print(f"col indices without hash: {col_indices_without_hash}")

# identify all coordinates containing a '#'
hash_coords = []
for j in range(len(grid)):
    for i in range(len(grid[0])):
        if grid[j][i] == "#":
            hash_coords.append((i, j))


# get all unique combinations of coordinates and calculate the distance
def get_distances(expansion_mult):
    total_manhattan_distance = 0
    for ind, coord in enumerate(hash_coords):
        for other_coord in hash_coords[ind + 1 :]:
            # calculate the distance
            x_dist = abs(coord[0] - other_coord[0])
            y_dist = abs(coord[1] - other_coord[1])
            # count col_indices between coord and other_coord
            col_indices_between = [
                col_ind
                for col_ind in col_indices_without_hash
                if col_ind > coord[0]
                and col_ind < other_coord[0]
                or col_ind < coord[0]
                and col_ind > other_coord[0]
            ]
            x_dist += len(col_indices_between) * expansion_mult
            row_indices_between = [
                row_ind
                for row_ind in row_indices_without_hash
                if row_ind > coord[1]
                and row_ind < other_coord[1]
                or row_ind < coord[1]
                and row_ind > other_coord[1]
            ]
            y_dist += len(row_indices_between) * expansion_mult

            total_manhattan_distance += x_dist + y_dist
    return total_manhattan_distance


print(f"total manhattan distance: {get_distances(1)}")
print(f"total manhattan distance: {get_distances(999999)}")

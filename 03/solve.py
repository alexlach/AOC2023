rows = open("03/input.txt").read().split("\n")

number_locations = []
for row, line in enumerate(rows):
    col = 0
    while col < len(line):
        char = line[col]
        if char.isdigit():
            number = char
            start_col = col
            col += 1
            # Check for multi-digit numbers
            while col < len(line) and line[col].isdigit():
                number += line[col]
                col += 1
            number_locations.append((number, row, start_col))
        else:
            col += 1


def has_adjacent_symbol(num_str, row, col):
    start_row = max(0, row - 1)
    start_col = max(0, col - 1)
    end_row = min(len(rows) - 1, row + 1)
    end_col = min(len(rows[0]) - 1, col + len(num_str))

    for r in range(start_row, end_row + 1):
        for c in range(start_col, end_col + 1):
            if not rows[r][c].isdigit() and not rows[r][c] == ".":
                return True
    return False


schematic_nums = []
for number_loc in number_locations:
    number, row, col = number_loc
    if has_adjacent_symbol(number, row, col):
        schematic_nums.append(int(number))

print(sum(schematic_nums))

# Part 2
asterisk_locations = []
for row, line in enumerate(rows):
    for col, char in enumerate(line):
        if char == "*":
            asterisk_locations.append((row, col))

powers = []
for asterisk in asterisk_locations:
    adj_nums = []
    ast_row, ast_col = asterisk
    for number_loc in number_locations:
        number, row, col = number_loc
        if abs(ast_row - row) <= 1:
            if ast_col >= col - 1 and ast_col <= col + len(number):
                adj_nums.append(int(number))
    if len(adj_nums) == 2:
        powers.append(adj_nums[0] * adj_nums[1])
print(sum(powers))
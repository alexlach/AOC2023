values = open("01/input.txt").read().split("\n")

# part 1
numbers = []
for value in values:
    value = [i for i in value if i.isnumeric()]
    first = value[0]
    last = value[-1]
    numbers.append(int(first + last))
print(f"Sum of calibration values is {sum(numbers)}.")

# part 2
vals_dict = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
}


def find_calibration_val(value, forwards=True):
    for i in range(1, len(value) + 1):
        for valid_val in vals_dict.keys():
            if forwards:
                if value[:i].endswith(valid_val):
                    return vals_dict.get(valid_val)
            else:
                if value[-i:].startswith(valid_val):
                    return vals_dict.get(valid_val)


calib_vals = []
for value in values:
    start_val = find_calibration_val(value, forwards=True)
    end_val = find_calibration_val(value, forwards=False)
    calib_vals.append(int(str(start_val) + str(end_val)))

print(f"Sum of calibration values is {sum(calib_vals)}.")

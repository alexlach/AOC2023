sequences = [[int(i) for i in line.split(" ")] for line in open('09/test.txt')]
# part 1

def part1(nums):
    right_sum = 0
    for nums in sequences:
        seq_hist = [nums]
        # get to the bottom of the sequence
        while max(nums) != 0 or min(nums) != 0:
            new_nums = []
            for i in range(len(nums) - 1):
                new_nums.append(int(nums[i + 1]) - int(nums[i]))
            nums = new_nums
            seq_hist.append(nums)
        
        # add one record to each seq in seq_hist starting at the bottom
        seq_hist[-1].append(0)
        for i in range(len(seq_hist) - 2, -1, -1):
            seq_hist[i].append(seq_hist[i + 1][-1] + seq_hist[i][-1])
        right_sum += seq_hist[0][-1]

    return right_sum

print(part1(sequences))

# part 2
sequences = [seq[::-1] for seq in sequences]  # reverse the sequences
print(part1(sequences))
nums = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]

for i in nums:
    if i == int(0):
        nums.remove(0)
        nums.append(0)


print(nums)



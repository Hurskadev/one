import random
nums = []
for i in range(random.randint(3, 10)):
    nums.append(random.randint(1, 10))
print(nums)
indexes = [0, 2, -2]
result = []
for idx in indexes:
        result.append(nums[idx])
print(result)





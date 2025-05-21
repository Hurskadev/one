nums = []
if len(nums) == 0:
       result = 0
sum_nums = 0
for i in range(0, len(nums), 2):
    sum_nums = sum_nums + nums[i]
    result = sum_nums * nums[-1]
print(result)
nums = [12, 3, 4, 10]
#nums = [1]
#nums = []
#nums = [12, 3, 4, 10, 8]
if len(nums) > 0:
    nums.insert(0, nums[-1])
   # print(nums)
    nums.pop()
    print(nums)
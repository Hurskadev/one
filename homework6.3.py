nums = int(input("Enter your number: "))

while nums > 9:
    result = 1


    for digit_char in str(nums):
        digit = int(digit_char)
        result *= digit

    nums = result

print(nums)
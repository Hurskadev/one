def common_elements():
    multiple_of_three = [num for num in range(100) if num % 3 == 0]
    multiple_of_five = [num for num in range(100) if num % 5 == 0]
    set_three = set(multiple_of_three)
    set_five = set(multiple_of_five)
    common = set_three & set_five
    return common

assert common_elements() == {0, 75, 45, 15, 90, 60, 30}
print("Ok")
number = int(input("Enter a number: "))
n1 = number % 10
number //= 10
n2 = number % 10
number //= 10
n3 = number % 10
number //= 10
n4 = number % 10
number //= 10
n5 = number % 10
result = n1 * 10000 + n2 * 1000 + n3 * 100 + n4 * 10 + n5
print(result)
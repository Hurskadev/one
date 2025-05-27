import string

example = input("Enter your example: ")
example = example.strip()
start, end = example.split('-')
start_index = string.ascii_letters.index(start)
end_index = string.ascii_letters.index(end)
if start_index <= end_index:
    result = string.ascii_letters[start_index:end_index+1]
else:
    result = string.ascii_letters[start_index:end_index - 1:-1]

print(result)

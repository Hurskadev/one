n1 = int(input("Select first number: "))
n2 = int(input("Select second number: "))
operation = input("Select action (+, -, *, /): ")
if operation == "+":
     result = n1 + n2
     print(result)
elif operation == "-":
    result = n1 - n2
    print(result)
elif operation == "*":
     result = n1 * n2
     print(result)
elif operation == "/":
  if n2 != 0:
      result = n1 / n2
      print(result)
  else:
      print("error")
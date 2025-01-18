
n1 = int(input("Enter the first number:"))
n2 = int(input("Enter the second number:"))

try:
  print(f"Result: {n1 / n2}")
except ZeroDivisionError:
  print("Cannot divide by zero!")
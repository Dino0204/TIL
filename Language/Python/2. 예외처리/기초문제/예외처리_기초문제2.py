
try:
  n = int(input("Enter a number:"))
  print(f"Entered number: {n}")
except ValueError:
  print("Invalid Input!")
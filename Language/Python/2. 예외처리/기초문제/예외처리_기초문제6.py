try:
  n = int(input("Enter a positive number: "))
  if n <= 0:
    raise ValueError("The number is not positive.")
  print("Positive number entered.")
except ValueError as e:
  print(f"Error: {e}")
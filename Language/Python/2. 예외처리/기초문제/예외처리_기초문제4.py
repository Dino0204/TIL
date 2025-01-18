my_list = [1,2,3]

try:
  print(my_list[5])
except IndexError as e:
  print(f"Error: {e}")
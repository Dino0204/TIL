my_list = ["10","20","thirty","40"]

n = int(input("Enter an index:"))

try:
  print(f"Converted number: {int(my_list[n])}")
except IndexError:
  print("Index out of range!")
except ValueError:
  print("Cannot convert element to integer!")
except TypeError:
  print("Invalid type encountered!")
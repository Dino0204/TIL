class MenuItem:
  def __init__(self,name,price,category):
    self.name = name
    self.price = price
    self.category = category
  def details (self):
    return f"Item: {self.name}, Price: {self.price}원, Category: {self.category}"


class Order:
  def __init__(self):
    self.items = []
    self.discount_num = 0
  
  def add_item(self,item):
    self.items.append(item)
    return f"{item.name} added to the order."
  
  def remove_item(self,item_name):
    for item in self.items:
      if item.name == item_name:
        self.items.remove(item)
        return f"{item_name} removed from the order."
    return f"{item_name} is not in the order."
  
  def calculate_total(self):
    total = 0
    for item in self.items: total += item.price
    return f"Total price after {self.discount_num}% discount: {total - (total * self.discount_num / 100)}원"
  
  def list_items(self):
    return "\n".join([item.details() for item in self.items])
  
  def list_items_by_category(self):
    categories = {}
    
    for item in self.items:
      if not item.category in categories:
        categories[item.category] = []
      categories[item.category].append(item)
    
    list_items = []
    
    for category in categories:
      list_items.append(f"Category: {category}")
      for item in self.items:
        if item.category == category:
          list_items.append(item.details())
    
    return f"\n".join(list_items)
  
  def apply_discount(self,discount_num):
    self.discount_num = discount_num
    return f"{discount_num}% discount has been applied to the order."

menu_item1 = MenuItem("Pizza", 15000, "Main Course")
menu_item2 = MenuItem("Pasta", 12000, "Main Course")
menu_item3 = MenuItem("Caesar Salad", 8000, "Appetizer")
menu_item4 = MenuItem("Ice Cream", 5000, "Dessert")

order = Order()

print(order.add_item(menu_item1))
print(order.add_item(menu_item2))
print(order.add_item(menu_item3))
print(order.add_item(menu_item4))

print(order.list_items()) 

print(order.list_items_by_category())
print(order.remove_item("Pizza"))
print(order.list_items_by_category())

print(order.calculate_total())
print(order.apply_discount(10))
print(order.calculate_total())
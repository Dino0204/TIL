# Fruit 클래스

# 속성
# 1. name
# 2. color

# 메서드
# 1. "It tastes good." taste 메서드

# Apple 클래스(Fruit 상속)

# 속성
# 1. variety

# 메서드
# 1. "This [variety] apple tastes sweet." taste 메서드

# Banana 클래스(Fruit 상속)

# 속성
# 1. length

# 메서드
# 1. "This banana tastes creamy." taste 메서드

class Fruit:
  def __init__(self, name, color):
    self.name = name
    self.color = color

  def taste(self):
    print("It tastes good.")  

class Apple(Fruit):
  def __init__(self, name, color, variety):
    super().__init__(name, color)
    self.variety = variety

  def taste(self):
    print(f"This {self.variety} apple tastes sweet.")

class Banana(Fruit):
  def __init__(self, name, color, length):
    super().__init__(name, color)
    self.length = length

  def taste(self):
    print("This banana tastes creamy.") 

apple = Apple("Apple", "Red", "Honeycrisp")
apple.taste()

banana = Banana("Banana", "Yellow", 15)
banana.taste()
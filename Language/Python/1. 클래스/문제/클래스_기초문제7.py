# Computer 클래스

# 속성
# 1. brand
# 2. model

# 메서드
# 1. "[brand] [model] is starting."을 출력하는 start 메서드

# Laptop 클래스(Computer 클래스 상속)

# 속성
# 1. battery_life

# 메서드
# 1. "[brand] [model] is starting. Battery life: [battery_life]"을 출력 (start 메서드 오버라이딩)

class Computer:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def start(self):
    print(f"{self.brand} {self.model} is starting.")

class Laptop(Computer):
  def __init__(self, brand, model, battery_life):
    super().__init__(brand, model)
    self.battery_life = battery_life

  def start(self):
    print(f"{self.brand} {self.model} is starting. Battery life: {self.battery_life}")


laptop = Laptop("Apple", "MacBook Pro", "10 hours")
laptop.start() 
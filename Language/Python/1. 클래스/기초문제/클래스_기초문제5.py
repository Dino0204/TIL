# Bird 클래스

# 속성
# 1. name
# 2. color

# 메서드
# 1. "[name] is flying"을 출력하는 fly 메서드

# Eagle 클래스(Bird 클래스 상속)

# 속성
# 1. speed

# 메서드
# 1. "Flying at [speed]km/hr."를 출력(fly 메서드 오버라이딩)

class Bird:
  def __init__(self, name, color):
    self.name = name
    self.color = color

  def fly(self):
    print(f"{self.name} is flying")

class Eagle(Bird):
  def __init__(self, name, color, speed):
    super().__init__(name, color)
    self.speed = speed

  def fly(self):
    print(f"Flying at {self.speed}km/hr.")

bird = Bird("Bird", "Blue")
bird.fly()

eagle = Eagle("Eagle", "Brown", 100)
eagle.fly()
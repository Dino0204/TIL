# CAR 클래스

# 속성
# 1. 자동차 모델을 나타내는 model 속성
# 2. 자동차 색상을 나타내는 color 속성
# 3. 자동차 속도를 나타내는 speed 속성

# 메서드
# 1. 자동차의 속도를 100으로 설정하는 drive 매서드
# 2, 자동차의 속도를 설정하는 changeSpeed 매서드

class Car:
  def __init__(self, model, color, speed):
    self.model = model
    self.color = color
    self.speed = speed

  def drive(self):
    self.speed = 100
  
  def changeSpeed(self, speed):
    self.speed = speed

ferrari = Car('Ferrarri', 'Red', 200)
print(f"차 모델은 {ferrari.model} 컬러는 {ferrari.color} 속도는 {ferrari.speed} 입니다.")

ferrari.drive()
print(f"차 모델은 {ferrari.model} 컬러는 {ferrari.color} 속도는 {ferrari.speed} 입니다.")

ferrari.changeSpeed(300)
print(f"차 모델은 {ferrari.model} 컬러는 {ferrari.color} 속도는 {ferrari.speed} 입니다.")
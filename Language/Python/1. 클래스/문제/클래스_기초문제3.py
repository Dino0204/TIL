# Calculator 클래스

# 속성
# 1. 계산 결과를 저장하는 result 속성 (초기값 0)

# 메서드
# 1. result값에 num값을 더한 후 반환하는 add 메서드

class Calculator:
  def __init__(self):
    self.result = 0

  def add(self, num):
    self.result += num
    return self.result

cal1 = Calculator()
cal2 = Calculator()

# cal1
print(cal1.add(1))
print(cal1.add(2))
print(cal1.add(3))

# cal2
print(cal2.add(4))
print(cal2.add(5))
# Person 클래스

# 속성
# 1. name
# 2. age

# 메서드
# 1. "My name is [name] and I'm [age] years old."를 출력하는 introduce_self 메서드

# Student 클래스(Person 클래스 상속)

# 속성
# 1. grade (초기값 A)

# 메서드
# 1. "I'm studying. I'm in [A] grade"를 출력하는 study 메서드

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def introduce_self(self):
    print(f"My name is {self.name} and I'm {self.age} years old.")

class Student(Person):
  def __init__(self, name, age, grade='A'):
    super().__init__(name, age)
    self.grade = grade

  def study(self):
    print(f"I'm studying. I'm in {self.grade} grade.")

p1 = Person('일준혁',20)
p1.introduce_self()

std1 = Student('이준혁',17,'3rd')
std1.introduce_self()
std1.study()

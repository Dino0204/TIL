# Unit 클래스

# 속성
# 1. name
# 2. power

# 메서드
# 1. "[name]이(가) 공격을 수행합니다. [전투력:[power]]"를 출력하는 attack 메서드
# 2. "이름:[name] / 전투력:[power]"를 출력하는 show_info 메서드

# Monster 클래스(Unit 클래스 상속)

# 속성
# 1. type_

# 메서드

class Unit:
  def __init__(self, name, power):
    self.name = name
    self.power = power

  def attack(self):
    print(f"{self.name}이(가) 공격을 수행합니다. [전투력:{self.power}]")

  def show_info(self):
    print(f"이름:{self.name} / 전투력:{self.power}")

class Monster(Unit):
  def __init__(self, name, power, type_):
    super().__init__(name, power)
    self.type_ = type_

  def show_info(self):
    print(f"이름:{self.name} / 전투력:{self.power} / 종류:{self.type_}")

unit = Unit("헐크", 50000)
unit.attack()

monster = Monster("투명인간", 10000, "중급")
monster.attack()
monster.show_info()
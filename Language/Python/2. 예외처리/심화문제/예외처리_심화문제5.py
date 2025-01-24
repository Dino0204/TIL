import random

answer = random.randint(1,100)
print("1부터 100 사이의 숫자를 맞춰보세요!")

while True:
  try:
    num = int(input("숫자를 입력하세요: "))
    
    if num > 100 or num < 1:
      raise ValueError("1 부터 100 사이의 값을 입력해주세요.")
    
    
    if num > answer:
      print("더 작은 숫자를 입력하세요.")
    elif num < answer:
      print("더 큰 숫자를 입력하세요.")
    
    elif num == answer:
      print("정답입니다!")
      break
      

  except ValueError as e:
    print(f"Error: {e}")
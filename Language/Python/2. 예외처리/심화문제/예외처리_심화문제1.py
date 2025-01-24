scores = []
while True:
  try:
    student_num = input("점수를 입력하세요 (종료는 'exit' 입력): ")
    
    if student_num == "exit":
        break
    
    if int(student_num) < 0 or int(student_num) > 100:
      raise ValueError("유효하지 않는 값의 범위 입니다.")

    scores.append(int(student_num))
  except ValueError as e:
    print(f"Error: {e}")

if scores:
  print(f"평균 점수: {sum(scores) / len(scores)}")
else:
  print("입력된 점수가 없습니다.")
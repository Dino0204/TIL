phonebook = {}

print("전화번호부 관리 시스템입니다. (종료: exit)")
while True:
  try:
    action = input("연락처 추가 또는 검색을 선택하세요 (추가: add, 검색: search, 종료: exit): ").lower()

    if action == "exit":
      break

    name = input("이름을 입력하세요: ")
    if action == "add":
      phone_number = input("전화번호를 입력하세요: ")
      phonebook[name] = phone_number
      
      print(f"연락처 {name}이(가) 추가되었습니다.")
    elif action == "search":
      if name in phonebook:
        print(f"{name}의 전화번호: {phonebook[name]}")
      else:
        raise Exception("'존재하지 않는 연락처입니다.'")
    else:
      print("올바른 선택을 해주세요.")
  
  
  except Exception as e:
    print(f"Error: {e}")
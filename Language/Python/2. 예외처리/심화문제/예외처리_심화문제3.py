shopping_list = set()
print("쇼핑 목록에 아이템을 추가하세요! (종료: exit)")

while True:
  try:
    item = input("추가할 아이템: ")
    
    if item == "exit":
      if not shopping_list:
        raise Exception("쇼핑 목록이 비어 있습니다. 아무것도 추가되지 않았습니다.")
      break
    
    if item in shopping_list:
      raise Exception("이미 존재하는 아이템입니다.")
    shopping_list.add(item)
    
    
  except Exception as e:
    print(f"Error: {e}")
print(f"쇼핑 목록: {shopping_list}")  
# 대출 : True
books = {"해리포터" : False,"반지의 제왕" : False,"어린 왕자" : False}

while True:
  try:
    action = input("대출 또는 반납을 선택하세요 (종료: exit): ").lower()
    
    if action == "exit":
      break
    
    book_name = input("책 이름을 입력하세요: ")
    
    
    if action == "대출":
      if not book_name in books:
        raise Exception("'존재하지 않는 책 입니다.'")
      
      books[book_name] = True
      print(f"{book_name} 대출 완료")
      
    elif action == "반납":
      if not book_name in books:
        raise Exception("'존재하지 않는 책 입니다.'")
      
      if books[book_name] == True:
        books[book_name] = False
        print(f"{book_name} 반납 완료")
      else:
        raise Exception("대출되지 않은 책 입니다.")
      
    else:
      print("올바른 선택을 해주세요.")
    
  except Exception as e:
    print(f"Error: {e}")
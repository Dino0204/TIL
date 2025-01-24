dictionary = {
  "apple":"A fruit that is usually red, green, or yellow.",
  "banana":"A long curved fruit with a yellow skin.",
  "orange":"A round citrus fruit with a tough bright reddish-yellow rind.",
}

while True:
  try:
    word = input("정의를 찾고 싶은 단어를 입력하세요 (종료: exit): ")
    
    if word == 'exit':
      break
    
    if word in dictionary:
      print(f"{word}: {dictionary[word]}")
    else:
      raise Exception("사전에 없는 단어입니다. 다시 입력하세요")
  except Exception as e:
    print(e)
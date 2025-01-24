products = ["노트북","스마트폰","태블릿","스마트워치","이어폰"]
print("상품을 주문하세요!")

while True:
  try:
    for i in range(len(products)):
      print(f"({i + 1}) {products[i]}",end=" ")
    print()
    
    product_num = int(input(">> "))
    print("------------------------------------------------------------")
    
    print(f"{products[product_num - 1]}을(를) 선택하셨습니다.")
    break
    
  except ValueError:
    print("숫자를 입력해주세요. 다시 선택하세요.")
  except IndexError:
    print("존재하지 않는 상품입니다. 다시 선택하세요.")
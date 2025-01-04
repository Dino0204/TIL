# 학생 클래스
class Std:
  # __~~~__ : 매직 메소드
  # __init__ : 생성자, 호출 시 초기화도 한꺼번에 이루어짐
  # self : 객체 자신을 가리키는 클래스 내의 첫번째 매개변수
  def __init__(self,name,kor,eng,math,sci):
    self.name=name
    self.kor=kor
    self.eng=eng
    self.math=math
    self.sci=sci
  
  def total(self):
    return self.kor + self.eng + self.math + self.sci
  
  def avg(self):
    return self.total()/4
  
  def print(self):
    print(self.name,self.total(),self.avg(),sep="\t")

# 학생 목록 클래스
class StudentList :
  def __init__(self):
    self.stds = [] # 학생 목록 빈 배열로 초기화
  
  def add(self,std):
    self.stds.append(std)
  
  def show(self):
    print("이름","총점","평균",sep="\t")
    # stds 배열 내의 학생 객체를 하나씩 꺼내서 출력
    for std in self.stds:
      std.print()

# 학생 객체 
std1 = Std("일준혁",90,80,70,60)
std2 = Std("이준혁",80,70,60,50)

# 학생 목록 객체 
std_list = StudentList()

std_list.add(std1)
std_list.add(std2)

std_list.show()
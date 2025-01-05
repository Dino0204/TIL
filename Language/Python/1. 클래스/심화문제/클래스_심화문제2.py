class Course:
  def __init__(self,title,instructor,duration):
    self.title = title
    self.instructor = instructor
    self.duration = duration
  def details(self):
    return f"Course: {self.title}, Instructor: {self.instructor}, Duration: {self.duration} hours"

class ProgrammingCourse(Course):
  def __init__(self,title,instructor,duration,language):
    super().__init__(title,instructor,duration)
    self.language = language
  def details(self):
    return f"{super().details()}, Language: {self.language}"

class MathCourse(Course):
  def __init__(self,title,instructor,duration,level):
    super().__init__(title,instructor,duration)
    self.level = level
  def details(self):
    return f"{super().details()}, Level: {self.level}"

class Student:
  def __init__(self,name):
    self.name = name
    self.courses = []
  
  def enroll(self,course):
    self.courses.append(course)
    return f"{self.name} has enrolled in {course.title}."
  
  def drop_course(self,course):    
    if course in self.courses:
      self.courses.remove(course)
      return f"{self.name} has dropped {course.title}."
    return f"{self.name} is not enrolled in {course.title}."
    
  def list_courses(self):
    if not self.courses:
      return f"{self.name} is not enrolled in any courses."
    return "\n".join([f"{course.details()}" for course in self.courses])

course = Course("Algorithm","Jennifet",17)
prog_course = ProgrammingCourse("Python 101","Alice",10,"Python")
math_course = MathCourse("Calculus I","Bob",15,"Undergraduate")
student = Student("John")

print(course.details())
print(prog_course.details())
print(math_course.details())

print(student.enroll(prog_course))
print(student.enroll(math_course))
print(student.list_courses())

print(student.drop_course(prog_course))
print(student.list_courses())
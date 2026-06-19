class Student:
  def __init__(self,name,roll_no,marks):
    self.name = name
    self.roll_no = roll_no
    self.marks = marks

  # Display student details:
  def display(self):
    print("Name:",self.name)
    print("Roll_no:",self.roll_no)
    print("Marks:",self.marks)

  # Update student marks:
  def update_marks(self,new_marks):
    self.marks = new_marks

      
s1 = Student("Tanii",71,90)
s2 = Student("Avniii",2,80)

students = [s1,s2]

# For Searching
roll = int(input("Enter a roll no to search:"))
found = False
for student in students:
    if student.roll_no == roll:
      found = True
      print("Student Found!")
      student.display()

if not found:
    print("Student Not Found")

# For deleting
roll = int(input("Enter a roll no to deleted:"))
for student in students:
    if student.roll_no == roll:
      students.remove(student)
      print("Student Deleted")
      
      print("Remaining Students:")

for student in students:
    student.display()

new_marks = 99
s1.update_marks(new_marks)

s1.display()
s2.display()
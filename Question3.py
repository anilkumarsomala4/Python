class Person:
    def __init__(self,name):
        self.name = name
class Student(Person):
    def __init__(self, name,roll_no):
        super().__init__(name)
        self.roll_no = roll_no
class CollegeStudent(Student):
    def __init__(self, name, roll_no,branch):
        super().__init__(name,roll_no)
        self.branch = branch
    def show(self):
        print("Name: ",self.name)
        print("Roll No: ",self.roll_no)
        print("Branch: ",self.branch)
c1=CollegeStudent("Anil","2311CS050045","CSE")
c2=CollegeStudent("Dhana sri","2311CS050068","CSE")
c1.show()
c2.show()
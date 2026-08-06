class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
        
    def anil(self):
        print(self.name ,self.marks)
s1 = Student("Anil",89)
s1.anil()
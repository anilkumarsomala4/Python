class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    def results(self):
        total = 0
        for i in (self.marks):
            total = total + i
        avg = total // 4
        print(f"{self.name} Your Total Scorce is {total} Out Of 400 and Avg is {avg}")
s1=Student("Anil",[88,89,97,86])
s2=Student("Yashwanth",[98,89,97,86])
s3=Student("Ajay",[78,89,87,86])
s1.results()
print()
s2.results()
print()
s3.results()
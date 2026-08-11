class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks=marks
    def grade(self):
        total = 0
        for i in self.marks:
            total = total + i
            avg = total / len(self.marks)
        if(avg>=90):
            print(avg,"A")
        elif avg >=75 and avg<90:
            print(avg,"B")
        elif avg>=60 and avg<75:
            print(avg,"C")
        elif avg>=40 and avg<60:
            print(avg,"D")
        else:
            print(avg,"F")
s1 = Student("Anil",[98,88,68,96,89])
s2 = Student("Dhana Sri",[80,85,90,96,99])
s3= Student("Jhon",[56,45,30,20,29])
s1.grade()
s2.grade()
s3.grade()        
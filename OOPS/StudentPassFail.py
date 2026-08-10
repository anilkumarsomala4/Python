class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    def check_results(self):
        total = 0
        for i in self.marks:
            total = total + i
        avg = total/len(self.marks)
        if(avg>=40):
            print(f"{self.name} Pass")
        else:
            print(f"{self.name} Fail")
s1=Student("Anil",[78,98,78])
s2=Student("Ganesh",[87,76,87])
s3=Student("Rahul",[45,30,21])
s1.check_results()
s2.check_results()
s3.check_results()
        


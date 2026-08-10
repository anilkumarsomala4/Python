class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks= marks
    def avg(self):
        sum = 0
        for i in self.marks:
            sum = sum + i
        a = sum // 3
        print(self.name,"Your Avg Score is ",a)
s1=Student("Anil",[86,98,85])
s2=Student("Dhana sri",[99,99,99])
s1.avg()
s2.avg()

        
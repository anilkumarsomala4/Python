class Employee:
    def __init__(self,name,basicsalary):
        self.name = name
        self.basicslary = basicsalary
    def calculate(self):
        HRA = (20/100)*self.basicslary
        DA = (10/100)*self.basicslary
        print(f"{self.name}")
        print("Basic:",self.basicslary)
        print("HRA: ",HRA)
        print("DA: ",DA)
        print("Total Salary: ",(self.basicslary+HRA+DA))
e1=Employee("anil",50000)
e1.calculate()

        
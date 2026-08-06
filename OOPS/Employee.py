class Employee:
    def __init__(self,Name,Salary,Department):
        self.Name = Name
        self.Salary = Salary
        self.Department = Department
    def show(self):
        print(self.Name)
        print(self.Salary)
        print(self.Department)
e1=Employee("Anil",75000,"HR")
e2=Employee("Dhana sri",50000,"IT")
e1.show()
print()
e2.show()
        
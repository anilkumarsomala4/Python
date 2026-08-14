class Bank:
    def __init__(self,Name, Acc, Pass):
        self.Name = Name
        self.Account_Number = Acc
        self.__password = Pass # Keeping Two underscore is northing but private so we can't access out side class

    def Show(self):
        print(self.Name,self.Account_Number,self.__password)# inside class it is possible
b1=Bank("Anil Kumar","24730100068","Anil@2004")
b2=Bank("Dhana Sri","24730100045","Dhana@2005")
b1.Show()
b2.Show()
print(b1.__password)# here is example of using private method outside class 
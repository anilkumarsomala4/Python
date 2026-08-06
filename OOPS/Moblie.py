class Moblie:
    def __init__(self,Company,RAM,Stroage):
        self.Company = Company
        self.RAM = RAM
        self.Stroage = Stroage
    def show(self):
        print(self.Company)
        print(self.RAM)
        print(self.Stroage)
m1 = Moblie("I Phone","8GB",256)
m1.show()
        
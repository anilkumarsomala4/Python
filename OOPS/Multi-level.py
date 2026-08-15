# Multi-level means inherting from pervious class 
class Bike:
    @staticmethod
    def start():
        print("Stating...")
    @staticmethod
    def stop():
        print("Stoping...")
class Honda(Bike):
    def __init__(self,Name):
        self.Name = Name
class Activa(Honda):
    def __init__(self,Name, type):
        super().__init__(Name)
        self.type=type
c1=Activa("Activa","6G Deluxe")
c1.start()
c1.stop()
print(c1.Name,c1.type)

        
        
# Inheritance means one class properties and methods can use of another class
# means like Parent class --> Child class
class Bike:
    @staticmethod
    def start():
        print("Strating...")
    @staticmethod
    def stop():
        print("Stop...")
class Honda(Bike):
    def __init__(self,type):
        self.type = type
b1=Honda("Activa")
b2=Honda("Bullet")
print(b1.start(),b1.type)
print(b2.stop(),b2.type)


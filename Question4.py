class Father:
    @staticmethod
    def driving():
        print("Driving...")
class Mother:
    @staticmethod
    def cooking():
        print("Cooking...")
class Child(Father, Mother):
    def playing(self):
        print("Playing...")
c1 = Child()
c1.driving()
c1.cooking()
c1.playing()
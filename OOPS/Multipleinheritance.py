# multiple inheritance means one child class from two or more parent classes
class Father:
    @staticmethod
    def driving():
        print("Mallesh Well in Driving")
class Mother:
    @staticmethod
    def cooking():
        print("Devi Well in Cooking")
class Child(Father, Mother):
    @staticmethod
    def eating():
        print("Anil Well in Eating")
c1=Child()
c1.driving()
c1.cooking()
c1.eating()
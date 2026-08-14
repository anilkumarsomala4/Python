# single inheritance one parent class and one child class
class Animal:
    @staticmethod
    def eating():
        print("Eating")
class Dog(Animal):
    @staticmethod
    def braking():
        print("Braking")
a1=Dog()
a1.eating()
a1.braking()
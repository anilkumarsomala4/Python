class Animal:
    @staticmethod
    def eating():
        print("Eating")
class Dog(Animal):
    @staticmethod
    def barking():
        print("Barking")
d1=Dog()
d1.eating()
d1.barking()
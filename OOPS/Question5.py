# hierarchical inheritance means it as one parent class and two or more child classes
class Animal:
    @staticmethod
    def eating():
        print("Eating..")
class Dog(Animal):
    @staticmethod
    def braking():
        print("Braking..")
class Cat(Animal):
    @staticmethod
    def meowing():
        print("Meowing")
d1=Dog()
c1=Cat()
d1.eating()
d1.braking()
c1.eating()
c1.meowing()
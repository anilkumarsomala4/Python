# Hybrid means it as one parent class and multiple child class and thatchild classes connected to hybrid class 
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
class Hybrid(Dog , Cat):
        @staticmethod
        def playing():
            print("Playing")
h1= Hybrid()
h1.eating()
h1.braking()
h1.meowing()
h1.playing()
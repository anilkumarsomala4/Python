class Vehicle:
    @staticmethod
    def start():
        print("Starting...")
    @staticmethod
    def stop():
        print("Stoping...")
class Car(Vehicle):
    @staticmethod
    def drive():
        print("Driving...")
c1 = Car()
c1.start()
c1.stop()
c1.drive()
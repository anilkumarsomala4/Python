class Car:
    def __init__(self,Brand,Colour,Price):
        self.Brand = Brand
        self.Colour = Colour
        self.Price = Price
    def display(self):
        print(self.Brand, self.Colour, self.Price)
c1=Car("BMW Car","Black",10000)
c1.display()


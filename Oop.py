class Car:
    count = 0

    def __init__(self, price, carno):
        self.price = price
        self.carno = carno

    def info(self):
        print("The car price is {} and it is {}".format(self.price, self.carno))


the_car = Car("Jiangsu", 1573)
the_car.info()

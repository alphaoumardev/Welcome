import types


class MyComputer:
    products = 0

    def __init__(self, cpu, ram, disk):
        self.cpu = cpu
        self.ram = ram
        self.disk = disk
        MyComputer.products += 1

    def information(self):
        print("My computer information are: cpu:{},ram: {}, disk: {}".format(self.cpu, self.ram, self.disk))

    def counting(self):
        print(self.cpu, self.ram, self.disk)


com = MyComputer("i7", 16, 512)
com.information()
# com.counting = types.MethodType(counting, com)
com.counting()

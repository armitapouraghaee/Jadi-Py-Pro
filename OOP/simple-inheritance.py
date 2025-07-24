class Computer:
    count = 0
    def __init__(self, ram, hard, cpu):
        self.ram = ram
        self.hard = hard
        self.cpu = cpu
    def value(self):
        return self.ram+self.hard+self.cpu
class Laptop(Computer):
    pass

pc1=Computer(12,2,4)
print(pc1.value())

laptop1 = Laptop(16,2,4)
print(laptop1.value())
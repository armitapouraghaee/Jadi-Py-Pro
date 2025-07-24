class Computer:
    count = 0
    def __init__(self, ram, hard, cpu):
        Computer.count +=1
        self.ram = ram
        self.hard = hard
        self.cpu = cpu
    def value(self):
        return self.ram+self.hard+self.cpu
    def __del__(self):
        Computer.count -=1
class Laptop(Computer):
    def value(self):
        return self.ram+self.hard+self.cpu+self.size

#***class Ipad(Computer,Laptop)***

pc1=Computer(12,2,4)
print(pc1.value())
del pc1

laptop1 = Laptop(16,2,4)
laptop1.size = 13
print(laptop1.value())
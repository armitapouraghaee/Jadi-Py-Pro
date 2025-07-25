class School:
    def __init__(self):
        self.number = int(input('ur number '))
        self.age = list(map(int, input('ur age ').split()))
        self.height = list(map(int, input('ur height ').split()))
        self.weight = list(map(int, input('ur weight ').split()))
    def average_age(self,):
        return float(sum(self.age) / self.number)

    def average_height(self):
        return float(sum(self.height) / self.number)

    def average_weight(self):
        return float(sum(self.weight) / self.number)
    
'''school = School()
print(school.average_age())
print(school.average_height())
print(school.average_weight())'''

class A(School):
    pass
class B(School):
    pass


a = A()
b = B()

print(a.average_age())
print(a.average_height())
print(a.average_weight())

print(b.average_age())
print(b.average_height())
print(b.average_weight())

if a.average_height() > b.average_height():
    print("A")
elif a.average_height() < b.average_height():
    print("B")
else:
    if a.average_weight() < b.average_weight():
        print("A")
    elif a.average_weight() > b.average_weight():
        print("B")
    else:
        print("Same")
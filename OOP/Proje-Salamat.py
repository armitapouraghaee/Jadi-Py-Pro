class School:
    def __init__(self):
        self.tedad = int(input('ur tedad '))
        self.sen = list(map(int, input('ur sen ').split()))
        self.ghad = list(map(int, input('ur ghad ').split()))
        self.vazn = list(map(int, input('ur vazn ').split()))
    def average_age(self,):
        return sum(self.sen) / self.tedad

    def average_height(self):
        # محاسبه میانگین قد
        return sum(self.ghad) / self.tedad

    def average_weight(self):
        return sum(self.vazn) / self.tedad
school = School()
print(school.average_age())
print(school.average_height())
print(school.average_weight())
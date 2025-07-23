class person:
    count = 0
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def get_name(self):
        print('name is %s' %self.name)
Armita = person ("Armita" , 24)
Armita.get_name()
class person:
    count = 0
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def get_name(self):
        print('name is %s' %self.name)
    def get_age(self):
        print('she is %s' %self.age)
    #or
    def get_info(self):
      print('name is %s and age is %i' %(self.name , self.age))
Armita = person ("Armita" , 24)
Armita.get_name()
Armita.get_age()
Armita.get_info()
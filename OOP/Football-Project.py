import random
class Person:
    def __init__(self,name):
        self.name = name 
class Footballer(Person):
    def __init__(self,name):
        super().__init__(name)
           
names_str="حسین - مازیار - اکبر - نیما -  مهدی - فرهاد - محمد - خشایار - میلاد - مصطفی - امین - سعید - پویا - پوریا - رضا - علی - بهزاد - سهیل - بهروز - شهروز - سامان - محسن"
names = names_str.split(" - ")
players= []
for name in names:
    player = Footballer(name)
    players.append(player)

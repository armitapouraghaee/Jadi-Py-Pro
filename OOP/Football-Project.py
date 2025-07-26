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

random.shuffle(players)
team_A = players[:11]    # 11 نفر اول تیم A
team_B = players[11:]    # 11 نفر دوم تیم B

print("Team A:", team_A)
print("Team B:", team_B)
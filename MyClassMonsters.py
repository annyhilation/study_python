import math
import random

class Monsters():
    name = ''
    power = 0
    agility = 0
    health = 0
    def out(self):
        print("Рррряя!")
    def ChooseMonster(self):
        listofmonsters = [['оса',1,2,10], ['сколопендра',2,3,20], ['волк',4,6,40], ['медведь',10,8,80]]
    #    print('listofmonsters', listofmonsters[0][0])
        r = random.randint(0,3)
        self.name = listofmonsters[r][0]
        self.power = int(listofmonsters[r][1])
        self.agility =int(listofmonsters[r][2])
        self.health = int(listofmonsters[r][3])
        return self.name, self.power, self.agility, self.health







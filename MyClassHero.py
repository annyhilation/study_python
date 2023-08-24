import math
import random

class Hero():
    name = ''
    spec = ''
    spec_text = ''
    power = 0
    agility = 0
    defence = 0
    level = 1
    xp = 0
    health = 100
    def out(self):
        print("Привет!")
    def DefineStats(self):
        if self.spec == '1':
            self.power = random.randint(9,18)
            self.agility = random.randint(4,15)
        else:
            self.power = random.randint(4,15)
            self.agility = random.randint(9,18)
        self.defence = self.power/2
        return self.power, self.agility
    def DefineSpec(self):
        self.spec = input("Выберите специализацию: 1-воин, 2-вор\n")
        spec_text_dict={'1':'Воин', '2':'Вор'}
        self.spec_text = spec_text_dict.get(self.spec)
        return self.spec_text
    def ChangeStats(self, newpower, newagility, newdefence):
        self.power = newpower
        self.agility = newagility
        self.defence = newdefence
    def Info(self):
        print("Имя: ", self.name, ", специализация: ", self.spec_text, ", сила: ", self.power, ", ловкость: ", self.agility, ", уровень: ", self.level, ", очки опыта: ", self.xp)
    def LevelUp(self):
        if self.xp>=self.level*10:
            self.level +=1
            self.health+=10
        else:
            self.level = self.level
        return self.level, self.health
    
    







from MyClassHero import Hero
from MyClassMonsters import Monsters
from MyClassActions import Actions

newgame = ''
newgame = input("Начать новую игру? y/n \n")

while newgame=='y':

    power = 0
    agility = 0
    spec = ''
    spec_text = ''
    hero = Hero()
    mon = Monsters()
    battle = Actions()
    hero_name = input("Введите имя персонажа: ")
    hero.name = hero_name
    hero.spec_text=hero.DefineSpec()
    print("Бросаем кубики на характеристики")
    characteristics = hero.DefineStats()
    print(hero.Info())
    cont = 'y'

    while cont=='y':
        #записываем статы героя в локальные переменные
        hero_power = hero.power
        hero_agility = hero.agility
        hero_defence = hero.defence
        hero_xp = hero.xp
        hero_health = hero.health
        hero_count_battle_actions = 0

        #записываем статы монстра в локальные переменные. монстр выбирается каждый проход цикла в шаге ниже
        mon_list = mon.ChooseMonster()
        mon_name = mon.name
        mon_power = mon.power
        mon_agility = mon.agility
        mon_health = mon.health


    #    print(hero_defence, hero_power, mon_power, hero_health, mon_health, hero_agility, mon_agility, hero_xp, sep = ',')
        #встреча с монстром
        print("Вы идете по лесу. \n По пути вам встречается ", mon_name)
        choice = input("Что будем делать? 1 - ударить, 2 - убежать\n")
        battle_info = str(battle.Battle(choice, hero_defence, hero_power, mon_power, hero_health, mon_health, hero_agility, mon_agility, hero_xp))
        battle_info=battle_info.replace('(','')
        battle_info=battle_info.replace(')','')
        l_battle_info = battle_info.split(',')

        #статы после встречи с монстром
        hero.xp = int(l_battle_info[2])
        hero.health = int(l_battle_info[0])
        hero_count_battle_actions = int(l_battle_info[3])
        message = l_battle_info[4]
        levelup = str(hero.LevelUp())
        levelup = levelup.replace('(','')
        levelup = levelup.replace(')','')
        l_levelup = levelup.split(',')
        hero.level = int(l_levelup[0])
        hero.health = int(l_levelup[1])
        print(message)
        print("Текущие очки опыта: ", hero.xp, ", текущее здоровье: ",hero.health, ", текущий уровень: ", hero.level, ". Потребовалось ходов: ", hero_count_battle_actions)

        if hero.health>0:
            cont = input("Идем дальше? y/n \n")
        else:
            cont='n'
            print("Приключение окончено. Но не расстраивайтесь, вы можете начать заново.")
    newgame = input("Начать заново? y/n \n")








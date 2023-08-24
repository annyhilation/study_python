class Actions():
    def Battle(choice, choices, defence_hero, power_hero, power_monster, health_hero, health_monster, agility_hero, agility_monster, hero_xp):
        health_hero_r = health_hero
        health_monster_r = health_monster
        hero_xp_r = hero_xp
        count_h_action = 0
        count_m_action = 0
        choice_r = choices
        check_run = 0
        message = ''
        while health_monster_r > 0 and health_hero_r>0 and check_run==0:
            if choice_r=='1':
                if int(agility_hero)>int(agility_monster) and count_h_action>=count_m_action: #если ловкость героя больше, он ходит первым, иначе первым ходит монстр
                    if  count_h_action<=count_m_action: #ходит герой
                        health_monster_r-=power_hero
                        count_h_action+=1
                        if health_monster_r <= 0:
                            hero_xp_r+=8
                            message = 'Монстр побежден!'
                    else:                               #ходит монстр
                        health_hero_r-=int(power_monster)
                        count_m_action+=1
                else:                                      #первым ходит монстр
                    health_hero_r-=int(power_monster)
                    count_m_action+=1
            else:
                check_run=1
                if int(agility_hero)>int(agility_monster):
                    hero_xp_r+=1
                    message = 'Вы успешно сбежали'
                else:
                    health_hero_r -= int(power_monster)
                    message = 'Монстр вас ударил'
            if health_hero_r<=0:
                message = 'Вас убили'
        return health_hero_r, health_monster_r, hero_xp_r, count_h_action, message





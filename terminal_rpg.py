from random import randint

# ------------------GLOBAL_COUNTERS------------------------------->
floor_number = 0
room_number = 0  # 5 - 9 комнат на этаж
step_counter = 0  # шаги действий
balance = 0
classes = {'mage': ['druid', 'sun_mage', 'dark_mage'],
           'melee': ['paladin', 'assassin', 'knight'],
           'ranged': ['musketeer', 'archer', 'hunter']
           }
enemies = ['slime', 'bandit', 'skeleton', 'skeleton_archer']

# ------------------CHANCES--------------------------------------->


def hit_chance(accuracy):
    chance_lst = [0] * 100
    for i in range(int(accuracy * 100)):
        chance_lst[i] = 1
    result = chance_lst[randint(0, 101)]
    return result


def avoid_chance(speed):
    chance_lst = [0] * 100
    for i in range(int(speed * 100)):
        chance_lst[i] = 1
    result = chance_lst[randint(0, 101)]
    return result


def critical_chance(crit_chance):
    chance_lst = [0] * 1000
    for i in range(int(crit_chance * 1000)):
        chance_lst[i] = 1
    result = chance_lst[randint(0, 1001)]
    return result


# ------------------PLAYER_ACTIONS------------------------------->


class Player:
    def __init__(self, clas, name, mana, hp, speed, acc, crit, luck,
                 char, phys_dam, mag_dam, phys_def, mag_def, lvl, xp, skil_lvl):
        self.clas = clas
        self.name = name
        self.mana = mana
        self.health = hp
        self.speed = speed
        self.accuracy = acc
        self.crit_chance = crit
        self.luck = luck
        self.charisma = char
        self.phys_damage = phys_dam
        self.mag_damage = mag_dam
        self.phys_def = phys_def
        self.mag_def = mag_def
        self.level = lvl
        self.experience = xp
        self.skills_lev = skil_lvl

    def player_mag_attack_damage(self, target):
        damage = int(target.mag_def - self.mag_damage)
        return damage

    def player_phys_attack_damage(self, target):
        damage = int(target.phys_def - self.phys_damage)
        return damage

    def player_phys_attack(self, target):
        result = self.player_phys_attack_damage(self, target) - target.phys_def
        if result >= 0:
            target.health -= result
        else:
            return 'No damage'

    # ------------------SKILLS------------------------------->

    def fireball(self):
        if critical_chance(self.crit_chance):
            damage = 2 * (self.mag_damage + int(round(self.mag_damage * 0.1 * self.level)))
        else:
            damage = self.mag_damage + int(round(self.mag_damage * 0.1 * self.level))
        return damage


# ------------------ENEMIES------------------------------->

class Enemy:
    def __init__(self, hp, mag_dam, phys_dam, acc, mag_def, phys_def, crit, lev, icon, exp):
        self.health = hp
        self.mag_damage = mag_dam
        self.phys_damage = phys_dam
        self.accuracy = acc
        self.mag_def = mag_def
        self.phys_def = phys_def
        self.crit_chance = crit
        self.level = lev
        self.icon = icon
        self.exp = exp

    def enemy_phys_attack(self):
        if hit_chance(self.accuracy):
            if critical_chance(self.crit_chance):
                enemy_damage = 2 * (self.phys_damage + int(round(self.phys_damage * 0.1 * self.level)))
            else:
                enemy_damage = (self.phys_damage + int(round(self.phys_damage * 0.1 * self.level)))
        else:
            enemy_damage = 0
        return enemy_damage

    def enemy_mag_attack(self):
        if hit_chance(self.accuracy):
            if critical_chance(self.crit_chance):
                enemy_damage = 2 * (self.mag_damage + int(round(self.mag_damage * 0.1 * self.level)))
            else:
                enemy_damage = self.mag_damage + int(round(self.mag_damage * 0.1 * self.level))
        else:
            enemy_damage = 0
        return enemy_damage


# mag_damage = 0
# phys_damage = 10
# accuracy = 0.4
# mag_def = 5
# phys_def = 8
# crit_chance = 0.01
# level = 0
# icon = None
# exp = 10

slime = Enemy(20, 0, 10, 0.4, 5, 8, 0.01, 0, 'nothing', 10)

print('<' + '*' * 80 + '-' * 20 + '>')

print(slime.health)

from random import randint

# ------------------GLOBAL_COUNTERS------------------------------->
floor_number = 0
room_number = 0  # 5 - 9 комнат на этаж
step_counter = 0  # шаги действий
balance = 0
classes = ['mage', 'melee', 'ranged']


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


def fib(n):
    lst = [1, 1]
    for i in range(2, n):
        lst.append(lst[i - 1] + lst[i - 2])
    print(*lst)


# ------------------PLAYER_ACTIONS------------------------------->


class Player:
    def __init__(self, clas, name, mana, hp, speed, acc, crit, luck,
                 char, phys_dam, mag_dam, phys_def, mag_def, lvl, xp, skil_lvl, mxhp,
                 next_lvl_xp, full_mana):
        self.clas = clas
        self.name = name
        self.mana = mana
        self.max_health = mxhp
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
        self.next_lvl_xp = next_lvl_xp
        self.full_mana = full_mana

    def player_mag_attack_damage(self, target):
        damage = int(target.mag_def - self.mag_damage)
        return damage

    def player_phys_attack_damage(self, target):
        damage = int(target.phys_def - self.phys_damage)
        return damage

    def player_phys_attack(self, target):
        result = self.player_phys_attack_damage(target) - target.phys_def
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
    def __init__(self, hp, mag_dam, phys_dam, acc, mag_def, phys_def, crit, lev, exp, coins, mxhp):
        self.max_hp = mxhp
        self.health = hp
        self.mag_damage = mag_dam
        self.phys_damage = phys_dam
        self.accuracy = acc
        self.mag_def = mag_def
        self.phys_def = phys_def
        self.crit_chance = crit
        self.level = lev
        self.exp = exp
        self.coins = coins
        self.mxhp = mxhp

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

    def enemy_hp_calc(self):
        mxhp = self.health + floor_number * 5 + self.level * 2
        return mxhp

    enemies = ['slime', 'bandit', 'skeleton', 'skeleton_archer', 'dark_mage']

    e_mxhp = 1

    # mag_damage = 0


# phys_damage = 10
# accuracy = 0.4
# mag_def = 5
# phys_def = 8
# crit_chance = 0.01
# level = 0
# icon = None
# exp = 10
slime = Enemy(20, 5, 12, 0.6, 5, 10, 0.02, )

# ------------------GAME---------------------------------------------------------------------->
player = Player('mage', 'lox', 90, 80, 0.1, 0.7, 0.03, 2, 4, 8, 20, 10, 25, 1, 0, [0], 100, 75, 120)


def calculate(param):
    if param == 'hp':
        return (player.health * 100) // player.max_health
    else:
        return (player.mana * 100) // player.full_mana


def window():
    print('_' * 160)
    print('-' * 100, f'Floor:{floor_number} | Room:{room_number} | Step:{step_counter} | Balance:{balance}')
    print('Player:')
    print('<' + 'X' * calculate('hp') + '_' * (100 - calculate('hp')) + '>',
          f'Health: {player.health}/{player.max_health}')
    print('<' + '*' * calculate('mana') + '_' * (100 - calculate('mana')) + '>',
          f'Mana: {player.mana}/{player.full_mana}')
    print('\n' * 7)
    print('_' * 160)
    print('-' * 160)


window()

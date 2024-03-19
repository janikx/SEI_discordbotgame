import enum, random, sys
from copy import deepcopy

# GAME MODES
class GameMode(enum.IntEnum):
  adventure = 1
  boss = 2
  arena = 3

class Entity():
  
    def __init__(self, name, hp, max_hp, attack, defense, xp, gold):
        self.name = name
        self.hp = hp
        self.max_hp = max_hp
        self.attack = attack
        self.defense = defense
        self.xp = xp
        self.gold = gold

    def fight(self, other):
        defense = min(other.defense, 19) # cap defense value
        chance_to_hit = random.randint(0, 20-defense)
        if chance_to_hit:
            damage = self.attack
        else:
            damage = 0

        other.hp -= damage

        return (self.attack, other.hp <= 0) #(damage, fatal)

class Character(Entity):
   
    def __init__(self, name, hp, max_hp, attack, defense, chakra, level, xp, gold, inventory, mode, battling, user_id):
        super().__init__(name, hp, max_hp, attack, defense, xp, gold)
        self.chakra = chakra
        self.level = level

        self.inventory = inventory

        self.mode = mode
        self.battling = battling
        self.user_id = user_id

class Enemy(Entity):

    def __init__(self, name, max_hp, attack, defense, xp, gold):
        super().__init__(name, max_hp, max_hp, attack, defense, xp, gold)
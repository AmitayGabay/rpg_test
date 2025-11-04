import random
from core.monster import Monster

class Goblin(Monster):
    def __init__(self, name):
        weapon = random.choice(["knife", "sword", "ax"])
        hp = 20
        type = "goblin"
        speed = random.randint(5, 10)
        power = random.randint(5, 10)
        armor_rating = 1
        super().__init__(name, hp, type, speed, power, armor_rating, weapon)
import random
from core.monster import Monster

class Orc(Monster):
    def __init__(self, name):
        weapon = random.choice(["knife", "sword", "ax"])
        hp = 50
        type = "orc"
        speed = random.randint(0, 5)
        power = random.randint(10, 15)
        armor_rating = random.randint(2, 8)
        super().__init__(name, hp, type, speed, power, armor_rating, weapon)

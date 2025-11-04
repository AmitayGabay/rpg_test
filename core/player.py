import random
from core.entity import Entity

class Player(Entity):
    def __init__(self, name: str):
        profession = random.choice(["doctor", "fighter"])
        hp = 50
        if profession == "doctor":
            hp += 10
        speed = random.randint(5, 10)
        power = random.randint(5, 10)
        if profession == "fighter":
            power += 2
        armor_rating = random.randint(5, 15)
        super().__init__(name, hp, speed, power, armor_rating)
        self.profession = profession

    def speak(self):
        print(f"The player {self.name} saying hello to monsters!")

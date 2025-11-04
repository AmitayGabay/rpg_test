from abc import ABC
from core.entity import Entity

class Monster(Entity, ABC):
    def __init__(self, name: str, hp: int, type: str, speed: int, power: int, armor_rating: int, weapon: str):
        super().__init__(name, hp, speed, power, armor_rating)
        self.type = type
        self.weapon = weapon

    def speak(self):
        print(f"{self.type} {self.name} angry!")


from abc import ABC, abstractmethod

class Entity(ABC):
    def __init__(self, name: str, hp: int, speed: int, power: int, armor_rating: int):
        self.name = name
        self.hp = hp
        self.speed = speed
        self.power = power
        self.armor_rating = armor_rating

    def attack(self, target, game_instance):
        attack_roll = game_instance.roll_dice(20) + self.speed
        print(f"{self.name} attacks {attack_roll}, opponent's armor: {target.armor_rating}")
        if attack_roll > target.armor_rating:
            damage_roll = game_instance.roll_dice(6) + self.power
            print(f"The damage caused is: {damage_roll}.")
            damage = damage_roll
            if hasattr(self, 'type') and self.type in ["orc", "goblin"]:
                damage *= Entity.calculate_weapon_multiplier(self.weapon)
                print(f"After calculating the damage the {self.type} monster inflicted, according to the weapon type - {self.weapon}, the damage is: {damage}")
            target.hp -= damage
            print(f"{self.name} hurt {target.name} and caused damage: {damage}, {target.name} has {target.hp} lives left.\n")
        else:
            print(f"{self.name} Missed the target: {target.name}.\n")

    @staticmethod
    def calculate_weapon_multiplier(weapon):
        if weapon == "knife":
            return 0.5
        elif weapon == "sword":
            return 1
        elif weapon == "ax":
            return 1.5
        return 1

    @abstractmethod
    def speak(self):
        pass



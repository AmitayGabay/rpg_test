import random
from core.player import Player
from core.orc import Orc
from core.goblin import Goblin


class Game:
    def __init__(self):
        self.player = Player("My-player")

    def start(self):
        print("Welcome to the battle with monsters!")
        player_name = input("Enter Your name:\n")
        self.player.name = player_name
        print(f"Your player is: {self.player.name} {self.player.profession}")
        print(f"HP: {self.player.hp}, Power: {self.player.power}, Speed: {self.player.speed}, Armor Rating: {self.player.armor_rating}")
        self.player.speak()
        while True:
            choice = Game.show_menu()
            if choice == '1':
                monster = Game.choose_random_monster()
                print(f"The monster is: {monster.type} {monster.name}")
                print(f"HP: {monster.hp}, Power: {monster.power}, Speed: {monster.speed}, Armor Rating: {monster.armor_rating}")
                print(f"You are going to fight with - {monster.type} {monster.name}!")
                self.battle(self.player, monster)
            elif choice == '2':
                print("Goodbye!")
                break
            else:
                print("Invalid selection. Please try again.")

    def roll_dice(self, sides):
        return random.randint(1, sides)

    def determine_first_attacker(self, entity1, entity2):
        roll1 = self.roll_dice(6) + entity1.speed
        roll2 = self.roll_dice(6) + entity2.speed

        print("The results of the die roll + the speed:")
        print(f"{entity1.name}: {roll1}")
        print(f"{entity2.name}: {roll2}\n")

        if roll1 > roll2:
            return entity1, entity2
        elif roll2 > roll1:
            return entity2, entity1
        else:
            if isinstance(entity1, Player):
                return entity1, entity2
            else:
                return entity2, entity1

    def battle(self, player, monster):
        attacker, defender = self.determine_first_attacker(player, monster)
        print(f"{attacker.name} starts first!")
        combat_over = False
        while not combat_over:
            print(f"Now it's the turn of: {attacker.name}.")
            print(f"The {attacker.name}'s HP is: {attacker.hp}, The {defender.name}'s HP is: {defender.hp}.")
            attacker.attack(defender, self)
            if defender.hp <= 0:
                print(f"{defender.name} was defeated.")
                print(f"{attacker.name} won the battle!!!\n\n")
                combat_over = True
            else:
                attacker, defender = defender, attacker

    @staticmethod
    def show_menu():
        print("main menu:")
        print("1. Go to battle")
        print("2. Exit")
        choice = input("Choose an option (1 or 2):\n")
        return choice

    @staticmethod
    def choose_random_monster():
        monster_type = random.choice(["Orc", "Goblin"])
        name_suffix = str(random.randint(1, 100))
        if monster_type == "Orc":
            return Orc(f"orc-{name_suffix}")
        elif monster_type == "Goblin":
            return Goblin(f"goblin-{name_suffix}")
        return None


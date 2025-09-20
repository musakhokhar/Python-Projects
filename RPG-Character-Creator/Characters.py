import random

elements = ["Air", "Earth", "Fire", "Water"]

class Character:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

        self.level = 1
        self.experience = 0
        self.health = 100
        self.mana = 0
        self.elemental_affinity = "None"
        self.gold_coins = 100
        
    def __str__(self):
        return f"{self.name} is a {self.gender} {self.race}.\nLevel: {self.level}\nExperience: {self.experience}\nHealth: {self.health}\nStrength: {self.strength}\nDefense: {self.defense}\nSpeed: {self.speed}\nIntelligence: {self.intelligence}\nMana: {self.mana}\nElemental Affinity: {self.elemental_affinity}\nGold: {self.gold_coins} coins"

class Human(Character):
    def __init__(self, name, gender):
        super().__init__(name, gender)

        self.race = "Human"
        self.strength = 3
        self.defense = 2
        self.speed = 2
        self.intelligence = 3

class Elf(Character):
    def __init__(self, name, gender):
        super().__init__(name, gender)

        self.race = "Elf"
        self.strength = 4
        self.defense = 1
        self.speed = 4
        self.intelligence = 5
        self.elemental_affinity = random.choice(elements)
        self.mana = 100

class Dwarf(Character):
    def __init__(self, name, gender):
        super().__init__(name, gender)

        self.race = "Dwarf"
        self.strength = 7
        self.defense = 6
        self.speed = 1
        self.intelligence = 3
        self.elemental_affinity = "Earth"
        self.mana = 100

def choose_character():

    player = None
    player_race = input("Choose your character's race (Human, Elf, Dwarf): ")

    if player_race.lower() == "human":
        name = input("Enter your character's name: ")
        gender = input("Enter your character's gender: ")
        if gender.lower() == "male" or gender.lower() == "female":
           player = Human(name, gender)
        else:
            print("Invalid gender for Human.")
            player = None
    elif player_race.lower() == "elf":
        name = input("Enter your character's name: ")
        gender = input("Enter your character's gender: ")
        if gender.lower() == "male" or gender.lower() == "female":
            player = Elf(name, gender)
        else:
            print("Invalid gender for Elf.")
            player = None
    elif player_race.lower() == "dwarf":
        name = input("Enter your character's name: ")
        gender = input("Enter your character's gender: ")
        if gender.lower() == "male" or gender.lower() == "female":
            player = Dwarf(name, gender)
        else:
            print("Invalid gender for Dwarf.")
            player = None
    if player:
        print("Character created successfully!")
        print(player)
    else:
        print("Character creation failed.")
        print("Please try again.")
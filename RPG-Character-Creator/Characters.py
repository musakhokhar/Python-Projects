import random

class Character:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

        self.level = 1
        self.experience = 0
        self.health = 100
    def __str__(self):
        return f"{self.name} is a {self.gender} {self.race}.\nLevel: {self.level}\nExperience: {self.experience}\nHealth: {self.health}\nStrength: {self.strength}\nDefense: {self.defense}\nSpeed: {self.speed}\nIntelligence: {self.intelligence}"
        

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

        self.elements = ["Air", "Earth", "Fire", "Water"]
        self.elemental_affinity = random.choice(self.elements)
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
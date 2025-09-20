from Characters import Human, Elf, Dwarf

print("Welcome to the RPG Character Creator!")

player_race = input("Choose your character's race (Human, Elf, Dwarf): ")
player = None

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
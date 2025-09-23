from People import Person, addperson, people

for i in range(5):
    addperson(people)

print("Here are the people in the database:")
print(people.keys())

for i in people:
    print(f"\n{people[i]}")

print("Enter the name of who you would like to see info about: ")
print(people[str(input())])

print("Enter the name of who you would like to add years to: ")
name = str(input())
print(f"{name} is now {people[name].addyears(5)} years old")
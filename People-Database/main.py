from People import Person, addperson, people

while True:
    print("What would you like to do?, add person(1), view database(2)")
    choice = int(input())
    if choice == 1:
        addperson(people)
    elif choice == 2:
        break
    else:
        print("Invalid choice, try again")

print("Here are the people in the database:")
print(people.keys())
print("Detailed info:")
for i in people:
    print(f"\n{people[i]}")

print("Enter the name of who you would like to see info about: ")
print(people[str(input())])

print("Enter the name of who you would like to add years to: ")
name = str(input())
print("How many years would you like to add?")
years = abs(int(input()))
print(f"{name} is now {people[name].addyears(years)} years old")